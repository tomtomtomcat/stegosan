from hashlib import sha256
from scapy.all import *
from random import randint

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

    ip = IP(src=src, dst=dst)
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

def send_packet(packet):
    send(packet)

def toggle_psh(packet):
    if packet[TCP].flags.S and not packet[TCP].flags.P:
        packet[TCP].flags="SP"
    else:
        packet[TCP].flags="S"

    print(str(packet[TCP].flags))

    return packet

def encode_hash(st, message):
    
    # for hashing: source ip, dst ip, sport, dport, seq, message
    params = str(st[IP].src) + " " + \
             str(st[IP].dst) + " " + \
             str(st[TCP].dport) + " " + \
             str(st[TCP].seq) + " " + \
             str(message)

    print("Parameters:\t\t", params)

    result = sha256(str(params).encode())

    digest = result.hexdigest()

    print("Hex digest:\t\t", digest)

    return digest

# TODO non-functional
def compare_bits(binarymessage, binarydigest):
    match = False

    for i in range(0,8):
        binarydigeststr = str(binarydigest)
        binarymessagestr = str(binarymessage)

        lastbits = binarydigeststr[len(str(binarydigest))-8:len(str(binarydigest))]
        digestasciichar = chr(int(lastbits))
        if digestasciichar == chr(int(binarymessagestr[i])):
                print("test")

    return match

## Code written by Xhonatan
## get the last 8 bits
def get_last_8bit(st):
    st = str(st)
    lastbits = st[-8:]
    return lastbits

## Code written by Xhonatan
def assemble(st1, st2):
    return st1 + st2