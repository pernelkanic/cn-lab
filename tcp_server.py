from socket import *

# Create a socket
s = socket(AF_INET, SOCK_STREAM)

# Bind the socket to a specific IP and port
s.bind(("127.0.0.1", 3002))

# Listen for incoming connections (with a maximum backlog of 1)
s.listen(1)

while True:
    # Accept incoming connection
    c, a = s.accept()
    print("Received connection from", a)
    
    # Receive data from the client
    data = c.recv(100).decode()
    print("Received data:", data)
    
    # Send a response back to the client
    response = "Hello from the server"
    c.send(response.encode('utf-8'))
    
    # Close the connection with the client
    c.close()
