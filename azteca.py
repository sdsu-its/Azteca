
import time




#remove the most recent message from the queue
def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)
    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
#start boto3 and connect to queue
from awsAuth import getClient
client = getClient()
queue_url = "https://sqs.us-west-1.amazonaws.com/277872029364/Azteca-Tasks"
waittime = 1
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})
from DeviceDriver import DeviceDriver, ImageDriver
driver=ImageDriver()
while (True):
        #read from queue for new events every waittime
        try:
                #get message from queue
                message = pop_message(client, queue_url)
                print(message)
                if message == "Turn on projector":
                        driver.turnOnProjector()
                        #start projector
                #add other command interfaces here
                time.sleep(waittime)
        #exit program
        except KeyboardInterrupt:
            exit()
        #continue program
        except:
                pass