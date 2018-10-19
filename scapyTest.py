from scapy.all import *

IP()

target = "www.github.com/30"

ip = IP(dst=target)

print (ip)
