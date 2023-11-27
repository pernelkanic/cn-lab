import socket import
struct import binascii
s= socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind(("127.0.0.1",0))
packet=s.recvfrom(65565)
print(packet)
ethernet_header = packet[0][0:14]
eth_header = struct.unpack("!6s6s2s", ethernet_header)
print("ETHERNET HEADER")
print("****************")
print("Destination Address")
print( binascii.hexlify(eth_header[0]))
print("Source Address")
print( binascii.hexlify(eth_header[1]))
print("Type")
print( binascii.hexlify(eth_header[2]))
print("IP HEADER")
print("*********")
ipheader = packet[0][14:34]
ip_header = struct.unpack("!12s4s4s", ipheader)
print("Destination Address")
print (socket.inet_ntoa(ip_header[1]))
print("Source Address")
print(socket.inet_ntoa(ip_header[2]))