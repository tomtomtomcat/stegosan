from hashlib import sha256
from scapy.all import *
import numpy as np
from random import randint,getrandbits

def take_input():
    st = input("Input a message to send: ")
    
    print("Message: \t\t", st)

    return st

def format_input(message, messagectr):

    messagehash = sha256(message + (str(messagectr)))
    result = ""

    result += "+"
    result += message
    result += "|"
    result += messagectr
    result += "|"
    result += messagehash[:4] + messagehash[-4:]
    result += "-"

    return result

def convert_hex_to_binary(st):
    b = bin(int(st, 16))
    
    # print("Last 8 bits of digest:\t", b[-8:])

    return b 

def convert_string_to_binary(st):
    st = list(map(bin,bytearray(st,'ascii')))
    
    print("Binary representation:\t", st)

    return st

def convert_binary_string_to_ascii(st):
    bi = chr(int(st,2))

    return bi


def establish_connection(src, dst, sport, dport):

    ip = IP(src=src, dst=dst)
    SYN = TCP(sport=sport, dport=dport, flags='S',seq=1000)
    SYNACK = sr1(ip/SYN)

    ACK = TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq+1)
    return send(ip/ACK)

def create_packet(src, dst, sport, dport, seq): 

    # for creating packet: source ip, dst ip, sport, dport, seq, random data
    packet = IP(src=src, dst=dst)/TCP(dport=dport, seq=seq,)/Raw(load=getrandbits(16))

    print("Packet summary:\t\t" + packet.summary() + " (Data: " + str(packet.load) + ")")

    return packet

def send_packet(packet):
    send(packet)

def toggle_psh(packet):
    if packet[TCP].flags.S and not packet[TCP].flags.P:
        packet[TCP].flags="SP"
    else:
        packet[TCP].flags="S"

    # print(str(packet[TCP].flags))

    return packet

def encode_hash(st):
    
    # for hashing: source ip, dst ip, sport, dport, seq, random data
    params = str(st[IP].src) + " " + \
             str(st[IP].dst) + " " + \
             str(st[TCP].dport) + " " + \
             str(st[TCP].seq) + " " + \
             str(st[TCP].payload)

    #print("Parameters:\t\t", params) # this is spam

    result = sha256(str(params).encode())

    digest = result.hexdigest()

    print("Hex digest:\t\t", digest)

    return digest

def compare_bits(binarymessage, binarydigest):
    match = False

    binarydigeststr = str(binarydigest)
    binarymessagestr = str(binarymessage)

    lastbits = binarydigeststr[-8:]

    # remove encode indicator and fill with leading zeros
    binarymessagestr = binarymessagestr[2:]
    binarymessagestr = binarymessagestr.zfill(8)
    print("Comparing " + lastbits + " and " + binarymessagestr) 
    if lastbits == binarymessagestr:
        match = True

    return match

def compare_bits_with_arr(binarymessage, binarydigest, arr):
    match = False

    binarydigeststr = str(binarydigest)
    binarymessagestr = str(binarymessage)

    # remove encode indicator and fill with leading zeros
    binarymessagestr = binarymessagestr[2:]
    binarymessagestr = binarymessagestr.zfill(8)

    count = 0
    for i in range(0,len(arr)):
        print("Comparing " + binarydigest[arr[i]] + " and " + binarymessagestr[i])
        if binarydigest[arr[i]] == binarymessagestr[i]:
            print("The two bits match.")
            count += 1
        else:
            print("The two bits don't match.")
            break
    
    if count == 8:
        match = True

    return match


def compare_hex(st1, st2):
    return st1[-4:] == st2[-4:]

def permu(n=8, k=256):
    perm_arr = []
    for i in range(0,n):
        redundancy = False
        while not redundancy:
            index = randint(0,k-1)
            if index not in perm_arr:
                perm_arr.append(index)
                redundancy = True

    print(perm_arr)
    return perm_arr

## Code written by Xhonatan
## get the last 8 bits
def get_last_8bit(st):
    st = str(st)
    lastbits = st[-8:]
    return lastbits

## Code written by Xhonatan
def assemble(st1, st2):
    return st1 + st2
