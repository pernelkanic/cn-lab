from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 3002))
op = "hai"
s.send(op.encode('utf-8'))
data = s.recv(100).decode()
print(data)
s.close()
