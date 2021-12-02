from args import *
from config import *
from helper import *

secret = ""
random.seed(secretkey)
permutation = generate_permutation_array()

def incoming_packets(pkt):
    print()

    global permutation
    random.seed(permutation[0])
    permutation = generate_permutation_array()
    print("Permutation array:\t", permutation)
    # filters incoming packets on source and destination
    # Or is just for testing
    #if ((pkt[IP].src == src) or (pkt[IP].dst == dst)):
    #if ((pkt[TCP].flags.P)):

    print("Marked packet found!")
    ## Example of what you see for summary
    ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding

    # digest = encode_hash(pkt, get_last_8bit(pkt))
    digest = encode_hash(pkt)
    print("Packet hash digest:",digest)
    bindigest = convert_hex_to_binary(digest)
   
    binstring = compare_and_extract(bindigest, permutation)

    char = convert_binary_string_to_ascii(binstring)
    # assemble character by character
    global secret
    secret += char
    #return encode_hash(pkt, get_last_8bit(pkt))

    # print secret as it's assembled
    print("Secret:", secret)


def receiver():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    # bind

    serverSocket.bind(("192.168.1.12", 5555));

    serverSocket.listen();
    serverSocket.accept();

    print("Client accepted, sniffing for marked packets...")
    
    #sniff(filter="ip and tcp and dst port 5555", prn=incoming_packets)
    sniff(lfilter=lambda s: TCP in s and s[TCP].flags==8 
            and s[IP].src==args.srcip and s[IP].dst==args.dstip, 
            prn=incoming_packets)
    #print(capture.show()

