from xmlrpc.server import SimpleXMLRPCServer
def is_even(n):
return n % 2 == 0
def add(a,b):
return a+b
def sub(a,b):
return a-b
def factorial(n):
factorial=1
for i in range(1,n+1):
factorial = factorial*i
return factorial
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port8000...")
server.register_function(is_even, "is_even")
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(factorial,"factorial")
server.register_function(factorial,"factorial")
server.serve_forever()


CLIENT SIDE:
import xmlrpc.client
proxy= xmlrpc.client.ServerProxy('http://localhost:8000/')
for i in range(5):
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
print("%d is even?: %d" % (a, (proxy.is_even(a))))
print("addition of given number is %d "%((proxy.add(a,b))))
print("sub of given number is %d "%((proxy.sub(a,b))))
print("factorial: %d" %((proxy.factorial(a))))
print("factorial: %d" %((proxy.factorial(b))))