
import time
#start connection to queue
from Client import Client
#read from queue for new events every waitTime
waitTime = 1
client = Client(waitTime)

#create a driver to translate messages from the queue into device instructions
import DeviceDriver
driver=DeviceDriver.ImageDriver()

while (True):
        try:
                #check queue for messages
                message = client.pop_message()
                print(message)
                if message == "Turn on projector":
                        driver.turnOnProjector()
                        #start projector
                #add other command interfaces here
                time.sleep(waitTime)
        #exit program
        except KeyboardInterrupt:
            exit()
        #continue program
        except:
                pass