from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import bigquery
from dotenv import load_dotenv
import kaggle
import pandas as pd

# Initialize credentials path and object to access GCP resources
credentials_path = 'C:/Users/spart/GCP/customer-churn-project-serv-accnt-creds/amazon-deliveries-project-c2fedb2a708b.json'
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Initialize variables to store dataset path and name, GCP project ID, dataset ID, 
# bucket, external and final table names 
dataset = 'mustafakeser4/bigquery-churn-dataset'
file_name = 'churn.csv'
local_path = f'./{file_name}'
project_id = 'amazon-deliveries-project'
dataset_id = 'customer_churn_data'
bucket_name = 'customer_churn_project_bucket'
external_table = ''
final_table = f'{dataset_id}.churn_features'


"""
    Function to download the dataset from Kaggle and upload it to Google Cloud Storage (GCS).
    This function uses the Kaggle API to download the dataset and then uploads it to a specified GCS bucket.
"""
def get_data():

    # Authenticate with Kaggle API
    kaggle.api.authenticate()

    # Download the dataset
    kaggle.api.dataset_download_files(dataset, path='.', unzip=True)

    # Download the dataset metadata
    kaggle.api.dataset_metadata(dataset, path='.')

    # Read in .csv file into dataframe
    df = pd.read_csv(local_path)

    # Set values for GCS bucket and blob name
    blob_name = file_name
    df.to_csv(blob_name, index=False)

    # Initialize Storage client to access GCP storage bucket
    client = storage.Client(credentials=credentials, project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_path)

    print(f'{bucket_name} was successfully updated.')


"""
    Function to create a query string for transforming the external table data.
    This function generates a SQL query string that performs various transformations on the data,
    including aggregating total minutes, calls, and charges for each customer.
    The query also includes case statements to categorize customers into different tiers based on their usage.
"""
def get_query_string(ext_table_id, ext_table):

    # Define the SQL query string
    return f"""
        WITH getTotals AS (
            SELECT  
                customer_id,
                TRUNC(SAFE_CAST(SUM(total_day_minutes + total_eve_minutes + total_intl_minutes + total_night_minutes) AS FLOAT64), 2) AS total_minutes,
                SAFE_CAST(SUM(total_day_calls + total_eve_calls + total_intl_calls + total_night_calls) AS INT64) AS total_calls,
                TRUNC(SAFE_CAST(SUM(total_day_charge + total_eve_charge + total_intl_charge + total_night_charge) AS FLOAT64), 2) AS total_charges
            FROM `{ext_table_id}`
            GROUP BY customer_id
        )
        
        SELECT
            TRIM(LOWER(final.customer_id)) AS customer_id,
            state,
            SAFE_CAST(account_length AS INT64) AS account_length,
            CASE WHEN international_plan = FALSE THEN 'No' ELSE 'Yes' END AS international_plan,
            CASE WHEN voice_mail_plan = FALSE THEN 'No' ELSE 'Yes' END AS voice_mail_plan,
            gt.total_minutes,
            gt.total_calls,
            gt.total_charges,
            SAFE_CAST(number_customer_service_calls AS INT64) AS number_customer_service_calls,            
            SAFE_CAST(churn AS INT64) AS churn
        FROM `{ext_table}` final
        LEFT JOIN getTotals gt
        ON final.customer_id = gt.customer_id
    """


"""
    Function to create external configurations and table, and final table for BigQuery.
    This function creates an external table in BigQuery that points to a CSV file in Google Cloud Storage (GCS).
    The CSV file is expected to have a header row, and the function will skip this row when reading the data.
    The external table is then used to transform the data and create a final native table in BigQuery.
    The final table, (churn_features) is then connected to in Power BI for analysis.
"""
def create_final_table():

    # Initialize BigQuery client
    client = bigquery.Client(credentials=credentials, project=project_id)

    # Define names for external table name & config variables
    external_table_id = f'{project_id}.{dataset_id}.external_churn_table'
    external_source_format = 'CSV'
    uri = [f'gs://{bucket_name}/{file_name}']

    # Define ExternalConfig object with external configurations
    external_job_config = bigquery.ExternalConfig(external_source_format)
    external_job_config.source_uris = uri # Specify the GCS URI of the source file
    external_job_config.options.skip_leading_rows = 1  # Skip the header row
    external_job_config.options.field_delimiter = ','  # Specify the delimiter
    external_job_config.autodetect = True  # Let BigQuery detect the schema

    # Create the external table
    external_table = bigquery.Table(external_table_id)
    external_table.external_data_configuration = external_job_config
    client.create_table(external_table, exists_ok=True)

    print(f'External table {external_table_id} created.')

    # Get query string to clean and transform the final table
    query = get_query_string(external_table_id, external_table)

    client.query(f"CREATE OR REPLACE TABLE `{project_id}.{final_table}` AS {query}").result()
    print(f'Cleaned data loaded into {final_table}')


if __name__ == "__main__":

    # Scrape the data from Kaggle and upload it to GCS
    get_data()

    # Create the external and final tables in BigQuery 
    create_final_table()