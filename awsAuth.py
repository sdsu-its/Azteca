import boto3

#credentials
access_key = "AKIAUBMTWV22FPEBQQ57"
access_secret = "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"
region ="us-west-1"


 

def getClient():
    return boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)