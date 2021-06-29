
import time
#start connection to queue
from Client import Client
#read from queue for new events every waitTime
waitTime = 1
client = Client(waitTime)
from multiprocessing import Process
import socket
def sendMessage(message):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.128.75.211',10000))
        s.sendall(message)
        return
#create a driver to translate messages from the queue into device instructions
import DeviceDriver
driver=DeviceDriver.DeviceDriver()
import socket
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.128.75.211',10000))
while (True):
        try:
                #check queue for messages
                intent_name = client.pop_message()
                
                p= Process(target=sendMessage,args=(intent_name.encode('utf-8'),))
                p.start()
                print(intent_name)       
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
