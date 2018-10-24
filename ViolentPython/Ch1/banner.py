import socket

socket.setdefaulttimeout(2)

s = socket.socket()

s.connect(("191.168.40.184", 80))

ans = s.recv(1024)

print (ans)
