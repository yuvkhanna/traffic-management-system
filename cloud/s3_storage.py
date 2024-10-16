import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

# S3 bucket name
BUCKET_NAME = 'traffic-management-cctv-storage'

# Function to upload a file to S3 (e.g., CCTV images)
def upload_file_to_s3(file_path, file_name):
    try:
        s3.upload_file(file_path, BUCKET_NAME, file_name)
        print(f"File {file_name} uploaded successfully to {BUCKET_NAME}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")

# Function to retrieve a file from S3
def download_file_from_s3(file_name, download_path):
    try:
        s3.download_file(BUCKET_NAME, file_name, download_path)
        print(f"File {file_name} downloaded successfully from {BUCKET_NAME}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
