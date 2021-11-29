from args import *
from config import *
from helper import *

def incoming_packets(pkt):
    src = "192.168.1.11"
    dst = "192.168.1.11"

    secret = ""
    # filters incoming packets on source and destination
    # Or is just for testing
    if ((pkt[IP].src == src) or (pkt[IP].dst == dst)):
        ## Example of what you see for summary
        ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
        # print(pkt[IP].summary())

        # digest = encode_hash(pkt, get_last_8bit(pkt))
        digest = encode_hash(pkt)
        binarydigest = convert_hex_to_binary(digest)
        
        # the last 8 binary characters should represent a character of the secret message
        char = convert_binary_string_to_ascii(binarydigest[-8:])
        # assemble character by character
        secret += char
        #return encode_hash(pkt, get_last_8bit(pkt))

        # print secret as it's assembled
        print(secret)

def receiver():
    src = args.srcip
    dst = get_if_addr(conf.iface)
    capture = sniff(filter="ip and tcp", prn=incoming_packets, count=5)
    print(capture.show())

"""
dst = get_if_addr(conf.iface)
print(dst)
scr = str("127.0.0.1")
sniff(filter="ip", prn=incoming_packets)
print("Test")
"""
