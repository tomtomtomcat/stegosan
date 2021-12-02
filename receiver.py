from args import *
from config import *
from helper import *

def incoming_packets(pkt):
    src = args.srcip
    dst = args.dstip
    sport = args.srcport
    dport = args.dstport
    secret = ""
    # filters incoming packets on source and destination
    # Or is just for testing
    #if ((pkt[IP].src == src) or (pkt[IP].dst == dst)):
    #if ((pkt[TCP].flags.P)):
    F = pkt['TCP'].flags
    if (pkt[IP].src == src) and (pkt[IP].dst == dst) and ('P' in F):
        random.seed(secretkey) # use preshared seed for permutation generator
        permutation = generate_permutation_array()
        print("Permutation array:\t", permutation)
        print(str(pkt[TCP].flags))
        ## Example of what you see for summary
        ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
        print(pkt[IP].summary(), pkt[TCP].load)

        # digest = encode_hash(pkt, get_last_8bit(pkt))
        digest = encode_hash(pkt)
        print("Packet hash digest:",digest)
        bindigest = convert_hex_to_binary(digest)
       
        binstring = compare_and_extract(bindigest, permutation)

        char = convert_binary_string_to_ascii(binstring)
        print(char)        
        # assemble character by character
        secret += char
        #return encode_hash(pkt, get_last_8bit(pkt))

        # print secret as it's assembled
        print(secret)

def receiver():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
     

    # Bind and listen

    serverSocket.bind(("192.168.1.12",5555));

    serverSocket.listen();
    (clientConnected, clientAddress) = serverSocket.accept();

    capture = sniff(filter="ip and tcp and dst port 5555", prn=incoming_packets)
    print(capture.show())

