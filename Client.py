
class Client:
    def __init__(self,waitTime):
        #set up connection to aws queue
        import boto3        
        region ="us-west-1"
        self.queue_url = "https://sqs.us-west-1.amazonaws.com/277872029364/Azteca-Tasks"
        import awsAuth
        self.client=boto3.client('sqs', aws_access_key_id = awsAuth.access_key, aws_secret_access_key = awsAuth.access_secret, region_name = region)
        self.client.set_queue_attributes(QueueUrl = self.queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waitTime)})

    def pop_message(self):
        response = self.client.receive_message(QueueUrl = self.queue_url, MaxNumberOfMessages = 10)
        #last message posted becomes messages
        message = response['Messages'][0]['Body']
        receipt = response['Messages'][0]['ReceiptHandle']
        self.client.delete_message(QueueUrl = self.queue_url, ReceiptHandle = receipt)
        return message
#start boto3 and connect to
        
