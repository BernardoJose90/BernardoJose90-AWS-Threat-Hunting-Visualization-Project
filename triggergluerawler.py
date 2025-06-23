import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    crawler_name = 'securityhub-findings-crawler'
    
    try:
        response = glue.start_crawler(Name=crawler_name)
        return {
            'statusCode': 200,
            'body': f'Crawler {crawler_name} started successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

