import struct
import socket
import binascii
s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind(('127.0.0.1',0))
p=s.recvfrom(65565)
print(p)
eth_head=p[0][0:14]
eh=struct.unpack('!6s6s2s',eth_head)
print("ETH HEAD")
print('des add:',binascii.hexlify(eh[0]))
print('src add:',binascii.hexlify(eh[1]))
print('type:',binascii.hexlify(eh[2]))