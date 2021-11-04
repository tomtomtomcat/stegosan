from helper import *

def incoming_packets(pkt):
    src = "35.50.12.218"
    dst = get_if_addr(conf.iface)
    # filters incomming packets on scource and destination
    # Or is just for testing
    if ((pkt[IP].src == src) or (pkt[IP].dst == dst)):
        ## Example of what you see for summary
        ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
        print(pkt[IP].summary())
        encode_hash(pkt, get_last_8bit(pkt))
        return encode_hash(pkt, get_last_8bit(pkt))

def receiver(args):
    src = args.srcip
    dst = get_if_addr(conf.iface)
    capture = sniff(filter='ip and tcp', prn=incoming_packets, count = 5)
    print(capture.show())

"""
dst = get_if_addr(conf.iface)
print(dst)
scr = str("127.0.0.1")
sniff(filter="ip", prn=incoming_packets)
print("Test")
"""
