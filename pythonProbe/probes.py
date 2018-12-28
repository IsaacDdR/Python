from scapy.all import *

def Packethandler(pkt) :
    if pkt.haslayer(Dot11ProbeReq) :
        if pkt.type == 0 and pkt.subtype == 4 :
            print ("Client with MAC: %s probing for SSID: %s" % (pkt.addr2, pkt.info))

sniff(iface="wlan0mon", prn = Packethandler)
