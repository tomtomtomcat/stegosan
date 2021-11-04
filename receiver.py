from helper import *

def incoming_packets(pkt):
    # filters incomming packets on scource and destination
    # Or is just for testing
    try:
        if ((pkt[IP].src == scr) or (pkt[IP].dst == dst) or (pkt[TCP].flags.S and pkt[TCP].flags.P)):
            ## Example of what you see for summary
            ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
            # print(pkt[IP].summary())
            ## Hex Packet Layout + Decoder
            ## https://hpd.gasmi.net/
            ## Notes for example Hex
            # hexData = hexdump(pkt)
            # print(bytes(pkt[TCP].payload))
            encode_hash(pkt, get_last_8bit(pkt))
    except:
        print("NO")

def receiver(args):
    src = args.srcip
    dst = get_if_addr(conf.iface)
    sniff(filter="ip", prn=incoming_packets)
    # print("Not implemented yet.")

"""
dst = get_if_addr(conf.iface)
print(dst)
scr = str("127.0.0.1")
sniff(filter="ip", prn=incoming_packets)
print("Test")
"""
