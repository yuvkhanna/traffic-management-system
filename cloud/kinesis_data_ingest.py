import boto3

def send_iot_data(data):
    kinesis_client = boto3.client('kinesis')
    response = kinesis_client.put_record(
        StreamName='traffic_data_stream',
        Data=data,
        PartitionKey='partition_key'
    )
    return response
