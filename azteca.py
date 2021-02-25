
import time
#start connection to queue
from Client import Client
#read from queue for new events every waitTime
waitTime = 1
client = Client(waitTime)

#create a driver to translate messages from the queue into device instructions
import DeviceDriver
driver=DeviceDriver.DeviceDriver()

while (True):
        try:
                #check queue for messages
                intent_name = client.pop_message()
                if intent_name == "ShowPC":
                        driver.ShowPC()
                elif intent_name == "LightsOn":
                        driver.LightsOn()
                elif intent_name == "LightsOff":
                        driver.LightsOff()
                elif intent_name == "ShowMac":
                        driver.ShowMac()
                elif intent_name == "ShowVGA":
                        driver.ShowVGA()
                elif intent_name == "ShowHDMI":
                        driver.ShowHDMI()
                elif intent_name == "MuteAudio":
                        driver.MuteAudio()
                elif intent_name == "UnmuteAudio":
                        driver.UnmuteAudio()
                #add other command interfaces here
                time.sleep(waitTime)
        #exit program
        except KeyboardInterrupt:
            exit()
        #continue program
        except:
                pass