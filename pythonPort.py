from socket import *

ip = raw_input("IP: ")
start = input("PUERTO DE INICIO: ")
end = input("PUERTO FINAL: ")

print ("Scaneo de IP: " , ip)

for port in range (start, end):
    print ("Probando puerto " + str(port) + "....")
    s=socket(AF_INET, SOCK_STREAM)
    s.settimeout(0)
    if(s.connect_ex((ip, port)) == 0):
        print ("Port ", port, "is open")
    s.close()
print  ("Scaneo completo")
