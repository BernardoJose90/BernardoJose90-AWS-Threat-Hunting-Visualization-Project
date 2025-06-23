import json
import boto3
import datetime

s3 = boto3.client('s3')
bucket_name = 'securitybucketss'  

def lambda_handler(event, context):
    timestamp = datetime.datetime.utcnow().isoformat()
    key = f'securityhub-findings/finding-{timestamp}.json'
    
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(event),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': f'Successfully stored finding to {key}'
    }

