import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('', 12000)
server_socket.bind(addr)
while True:
  print("Waiting to receive message from client")
  message,address = server_socket.recvfrom(1024)
  print("Received %s" %message)
  server_socket.sendto(message,address)
