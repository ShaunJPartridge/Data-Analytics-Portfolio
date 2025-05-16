from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import bigquery
from dotenv import load_dotenv
import kaggle
import os
import pandas as pd

# Get credentials for GCP
credentials_path = 'C:/Users/spart/GCP/customer-churn-project-serv-accnt-creds/amazon-deliveries-project-c2fedb2a708b.json'
# Create a credentials object
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Authenticate with Kaggle API
kaggle.api.authenticate()

# Initialize variables to store dataset, GCP project ID, and dataset ID
dataset = 'mustafakeser4/bigquery-churn-dataset'
file_name = 'churn.csv'
local_path = f'./{file_name}'
project_id = 'amazon-deliveries-project'
dataset_id = 'customer_churn_data'

# Download the dataset
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)

# Download the dataset metadata
kaggle.api.dataset_metadata(dataset, path='.')

# Read in .csv file into dataframe
df = pd.read_csv(local_path)

# Initialize variables for GCS bucket and blob name
bucket_name = 'customer_churn_project_bucket'
blob_name = 'churn.csv'
df.to_csv(blob_name, index=False)

# Initialize Storage client to access GCP storage bucket
client = storage.Client(credentials=credentials, project=project_id)
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(local_path)


# Function to create a BigQuery view so the external table can be connected to in
# Power BI
def create_view(table_id):

    # Initialize BigQuery client
    Client = bigquery.Client(credentials=credentials, project=project_id)

    # Define the view name and the SQL query to create it
    view_id = 'vw_churn_table'
    sql_query = f"""
        CREATE OR REPLACE VIEW `{project_id}.{dataset_id}.{view_id}` AS
        SELECT * FROM `{project_id}.{dataset_id}.{table_id}`
    """

    # Create the view
    Client.query(sql_query).result()  # Wait for the query to finish

    print(f'Created view {view_id}')


# Function to load the data into BigQuery using an External table
def create_table():

    # Initialize BigQuery client
    Client = bigquery.Client(credentials=credentials, project=project_id)

    # Define table name, ref, and the GCS URI of the file
    table_id = 'external_churn_table'
    table_ref = f'{project_id}.{dataset_id}.{table_id}'
    data_uri = f'gs://{bucket_name}/{blob_name}'

    # Configure the external data source
    external_config = bigquery.ExternalConfig('CSV')
    external_config.source_uris = [data_uri]
    external_config.options.skip_leading_rows = 1  # Skip the header row
    external_config.options.field_delimiter = ','  # Specify the delimiter
    external_config.autodetect = True # Let BiqQuery detect the schema

    # Create the external table
    table = bigquery.Table(table_ref)
    table.external_data_configuration = external_config
    
    try:
        # Try to fetch existing table
        existing_table = Client.get_table(table_ref)

        # Update the external configuration
        existing_table.external_data_configuration = external_config
        
        # Update the table
        updated_table = Client.update_table(existing_table, ['external_data_configuration'])
        print(f'Updated existing table: {updated_table.table_id}')
    except Exception as not_found:
        # If the table does not exist, create a new one
        created_table = Client.create_table(table)
        print(f'Created new table: {created_table.table_id}')

    # Create the view so the data can be accessed in Power BI
    create_view(table_id)


if __name__ == "__main__":
    # Create the table and view
    create_table()
