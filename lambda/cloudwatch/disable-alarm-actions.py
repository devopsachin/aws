import boto3
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    response = cloudwatch.disable_alarm_actions(
        AlarmNames=['alarm-names']
    )
