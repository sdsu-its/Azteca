
import time
#start connection to queue
from Client import Client
#read from queue for new events every waitTime
waitTime = 1
client = Client(waitTime)
from multiprocessing import Process
import socket
def sendMessage(message):
        
        print("sent message"+message) 
        return
#create a driver to translate messages from the queue into device instructions
import DeviceDriver
driver=DeviceDriver.DeviceDriver()
import socket
#s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('10.128.75.211',10000))
#s.sendall("connected".encode('utf-8'))
while (True):
        try:
                #check queue for messages
                intent_name = client.pop_message()
                
                #p= Process(target=sendMessage,args=(intent_name.encode('utf-8'),))
                #global s
                if intent_name:
                    #p= Process(target=sendMessage,args=(intent_name.encode('utf-8'),))
                    #p.start()
                    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(('10.128.75.211',10000))
                    s.sendall(intent_name.encode('utf-8'))
                    print(intent_name)       
                time.sleep(waitTime)
        #exit program
        except KeyboardInterrupt:
            exit()
        #continue program
        except Exception as e: pass
                
