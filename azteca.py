import boto3
import time
#credentials
access_key = "AKIAUBMTWV22FPEBQQ57"
access_secret = "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"
region ="us-west-1"
queue_url = "https://sqs.us-west-1.amazonaws.com/277872029364/Azteca-Tasks"
#remove the most recent message from the queue
def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
#start boto3 and connect to queue
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

waittime = 1
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})

while (True):
        #read from queue for new events every waittime
        print("Checking...")
        try:
                #get message from queue
                message = pop_message(client, queue_url)
                print(message)
                if message == "Turn on projector":
                        #start projector
                        projector='started'
                #add other command interfaces here
                time.sleep(waittime)
        #exit program
        except KeyboardInterrupt:
            exit()
        #continue program
        except:
                pass
