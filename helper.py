from scapy.all import *

def take_input():
    st = input("Input a message to send: ")
    
    print("Message: \t\t", st)

    return st

def convert_to_binary(st):
    # st = " ".join(f"{ord(i):08b}" for i in st) # string with space joining each byte 
    st = int("".join(f"{ord(i):08b}" for i in st)) # int
    
    print("Binary representation:\t", st)

    return st

def establish_connection(src, dst, sport, dport):

    ip = IP(src=src, dst=drc)
    SYN = TCP(sport=sport, dport=dport, flags='S',seq=1000)
    SYNACK = sr1(ip/SYN)

    ACK = TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq+1)
    return send(ip/ACK)

def create_packet(src, dst, sport, dport, seq=0): # TODO fix/remove default parameter for seq?
    seq = 1002 # TODO remove hardcoding of seq?

    # for creating packet: source ip, dst ip, sport, dport, seq
    packet = IP(src=src, dst=dst)/TCP(dport=dport, seq=seq)

    print("Packet summary:\t\t", packet.summary())

    return packet

def encode_hash(st, message):
    
    # for hashing: source ip, dst ip, sport, dport, seq, message
    params = str(st[IP].src) + " " + \
             str(st[IP].dst) + " " + \
             str(st[TCP].dport) + " " + \
             str(st[TCP].seq) + " " + \
             str(message)

    print("Parameters:\t\t", params)

    result = hashlib.sha256(str(params).encode())

    digest = result.hexdigest()

    print("Hex digest:\t\t", digest)

    return digest

# TODO finish and use
# ----- implement logic for comparing 8 bits -----
# def compare_bits(binarymessage, binarydigest):
#     for i in range(1,8):
#         print(i)
