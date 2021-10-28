from scapy.all import *

def incomming(pkt):
    # filters incomming packets on scource and destination
    # Or is just for testing
    if ((pkt[IP].src == "192.168.0.99") or (pkt[IP].dst == "192.168.1.78")):
        ## Example of what you see for summary
        ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
        print(pkt[IP].summary())

        ## Everything in the packet
        # print(pkt[IP].show())

        ## What is being sent
        ## Example of what you see
        ## b'\x01\xbb\x82^x\x18\x1aY\x98\xb9\xd0oP\x10\x04\x02\xf3%\x00\x00\x00\x00\x00\x00\x00\x00'
        print(pkt[IP].payload)

sniff(filter="ip", prn=incomming)