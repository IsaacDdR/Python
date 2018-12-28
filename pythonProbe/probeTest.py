import sys
from scapy.all import *

clientProbes = set()

def PacketHandler(pkt) :

        if pkt.haslayer(Dot11ProbeReq) :

            if pkt.info == 'smart.haus' :
                testcase = pkt.addr2 + '---' + pkt.info
                if testcase not in clientProbes :
                    clientProbes.add(testcase)
                    print ("Nuevo Dispositivo: " + pkt.addr2 + " " + pkt.info)


sniff(iface = sys.argv[1], count = int( sys.argv[2] ), prn = PacketHandler)
