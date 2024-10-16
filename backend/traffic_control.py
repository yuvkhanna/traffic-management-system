import boto3
import json

def control_traffic_signal(signal_id, action):
    # AWS IoT MQTT or similar
    iot_client = boto3.client('iot-data')
    response = iot_client.publish(
        topic=f'traffic/signals/{signal_id}',
        qos=1,
        payload=json.dumps({"action": action})
    )
    return response
