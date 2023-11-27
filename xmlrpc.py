SERVER SIDE:
from xmlrpc.server import SimpleXMLRPCServer
def list_length(a):
return len(a)
def list_maximum(a):
return max(a)
def list_minimum(a):
return min(a)
def list_to_set(a):
f=list(set(a))
return f
def list_concate(a,b):
return a+b
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port8000...")
server.register_function(list_length,"list_length")
server.register_function(list_maximum,"list_maximum")
server.register_function(list_minimum,"list_minimum")
server.register_function(list_to_set, "list_to_set")
server.register_function(list_concate, "list_concate")
server.serve_forever()

CLIENT SIDE:
import xmlrpc.client
proxy= xmlrpc.client.ServerProxy('http://localhost:8000/')
while True:
print("PRESS 1-->STRAT || 2--> STOP ")
c=int(input("ENTER YOUR CHOICE"))
a=[]
b=[]
if c==1:
print("ENTER THE ELEMENTS TO ADD FIRST LIST")
print("PRESS -1 TOEXIT THIS LIST")
while True:
d=int(input("--->"))
if d==-1:
break
a.append(d)
print("ENTER THE ELEMENTS TO ADD SECOND LIST")
print("PRESS -2 TOEXIT THIS LIST")
while True:
e=int(input("--->"))
if e==-2:
break
b.append(e)
if c==2:
break
print(a)
print(b)
print("list_length",proxy.list_length(a))
print("list_maximum",proxy.list_maximum(a))
print("list_minimum",proxy.list_minimum(a))
print("list_to_set",proxy.list_to_set(a))
print("list_concate",proxy.list_concate(a,b))