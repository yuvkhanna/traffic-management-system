import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# DynamoDB table where traffic data will be stored
TABLE_NAME = 'TrafficData'

# Function to insert real-time traffic data into DynamoDB
def insert_traffic_data(location, traffic_status, timestamp):
    try:
        table = dynamodb.Table(TABLE_NAME)
        response = table.put_item(
            Item={
                'location': location,
                'traffic_status': traffic_status,
                'timestamp': timestamp
            }
        )
        return response
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        return None

# Function to retrieve traffic data for a specific location
def get_traffic_data(location):
    try:
        table = dynamodb.Table(TABLE_NAME)
        response = table.get_item(
            Key={'location': location}
        )
        return response.get('Item', {})
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error: {e}")
        return None
