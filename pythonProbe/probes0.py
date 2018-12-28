from scapy.all import sniff

def PacketHandler(pkt):
    return

sniff(iface="wlp2s0", prn = PacketHandler, store=0)
