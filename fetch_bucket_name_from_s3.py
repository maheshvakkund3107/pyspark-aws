import boto3

if __name__ == '__main__':
    s3_client = boto3.client('s3')
    buckets = s3_client.list_buckets()['Buckets']
    print([bucket['Name'] for bucket in buckets])
