import socket
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.128.75.211',10000))
s.sendall("ShowMac".encode('utf-8'))