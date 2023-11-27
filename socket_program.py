import socket
data = 1234
data1 = socket.htonl(data)
print(data1)
print(socket.ntohl(data1))
