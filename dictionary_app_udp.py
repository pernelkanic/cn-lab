SERVER SIDE:
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('', 12000)
server_socket.bind(addr)
while True:
m,address = server_socket.recvfrom(1024)
n=m.decode()
a={'use':'utilize','destroy':'demolish','fall':'drop','decide':'choose','help':'serve','pla
n':'blueprint', 'show':'display','break':'smash','make':'create','hurry':'rush'}
g=a[n]

REG.NO.
NAME

43
server_socket.sendto(g.encode(),address)
CLIENT SIDE:
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
print("Enterthe Word")
w=input("-->",)
m=str.encode(w)
addr = ("127.0.0.1", 12000)
client_socket.sendto(m,addr)
data,server = client_socket.recvfrom(1024)
print("Meaning is %s",data)