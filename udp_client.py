import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'Test message. This will be echoed'
addr = ('127.0.0.1', 12000)
client_socket.sendto(message.encode('utf-8'),addr)
data,server = client_socket.recvfrom(1024)
print("received %s" % data)
client_socket.close()