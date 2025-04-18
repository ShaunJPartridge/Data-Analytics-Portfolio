from google.oauth2 import service_account
from google.cloud import storage
from dotenv import load_dotenv
import kaggle
import os

# Get credentials for GCP
credentials_path = 'C:/Users/spart/GCP/customer-churn-project-serv-accnt-creds/amazon-deliveries-project-c2fedb2a708b.json'
project_id = 'amazon-deliveries-project '
bucket_name = 'customer_churn_project_bucket'

# Create a credentials object
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Authenticate with Kaggle API
kaggle.api.authenticate()

# Download the dataset
kaggle.api.dataset_download_files('mustafakeser4/bigquery-churn-dataset',path='.', unzip=True)

# Download the dataset metadata
kaggle.api.dataset_metadata('mustafakeser4/bigquery-churn-dataset', path='.')

# Set client to access GCP storage bucket
client = storage.Client(credentials=credentials, project=project_id)
bucket = client.bucket(bucket_name)

# Read in .csv file into dataframe
for file in os.listdir('.'):
    if file.endswith('.csv'):
        csv_file = file

        # Upload the file to GCP storage
        blob = bucket.blob(csv_file)
        blob.upload_from_filename(csv_file)

# for debugging purposes
# file_name = csv_file
# print(f"File {file_name} successfully uploaded to gs://{bucket_name}/{file_name}")