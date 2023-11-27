from socket import*
s=socket(AF_INET,SOCK_STREAM)
s.bind(("",8000))
s.listen(5)
print("=================CALCULATOR================")
c,a=s.accept()
while True:
data=c.recv(100).decode()
if(data=="1")
f=("Enter 1st value")
c.send(f.encode('utf-8'))
d1=c.recv(100).decode()
print(d1)
d3=int(d1)
g=("Enter 2nd Value")
c.send(g.encode('utf-8'))
d2=c.recv(100).decode()
print(d2)
d4=int(d2)
ans=d3+d4
ans1=str(ans)
c.send(ans1.encode('utf-8'))
if(data=="2"):
f=("Enter 1st value")
c.send(f.encode('utf-8'))
d1=c.recv(100).decode()
print(d1)
d3=int(d1)
g=("Enter 2nd Value")
c.send(g.encode('utf-8'))
d2=c.recv(100).decode()
print(d2)
d4=int(d2)
ans=d3-d4
ans1=str(ans)
c.send(ans1.encode('utf-8'))
if(data=="3"):
f=("Enter 1st value")
c.send(f.encode('utf-8'))
d1=c.recv(100).decode()
print(d1)
d3=int(d1)
g=("Enter 2nd Value")
c.send(g.encode('utf-8'))
d2=c.recv(100).decode()
print(d2)
d4=int(d2)
ans=d3*d4
ans1=str(ans)
c.send(ans1.encode('utf-8'))
if (data=="4"):
f=("Enter1stvalue")
c.send(f.encode('utf-8'))
d1=c.recv(100).decode()
print(d1)
d3=int(d1)
g=("Enter 2nd Value")
c.send(g.encode('utf-8'))
d2=c.recv(100).decode()
print(d2)
d4=int(d2)
ans=d3/d4
ans1=str(ans)
c.send(ans1.encode('utf-8'))
if(data=="5"):
break

//client side
from socket import*
s=socket(AF_INET,SOCK_STREAM)
s.connect(("127.0.0.1",8000))
print("================CALCULATOR=================")
print("Enter Your Choice")
print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit")
while True:
msg=input("-->",)
s.send(msg.encode('utf-8'))
data=s.recv(100).decode()
print("<--",data)