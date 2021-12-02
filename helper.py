from hashlib import sha256
from scapy.all import *
import numpy as np
from random import randint,getrandbits


from config import *

def take_input():
    st = input("Input a message to send: ")

    return st

def format_input(message, messagectr):

    messagehash = sha256((message + (str(messagectr))).encode('utf-8'))
    result = ""

    result += "+"
    result += message
    result += "|"
    result += str(messagectr)
    result += "|"
    result += str(messagehash)[:4] + str(messagehash)[-4:]
    result += "-"

    return result

def convert_hex_to_binary(st):
    b = bin(int(st, 16))
    
    # print("Last 8 bits of digest:\t", b[-8:])

    return b 

def convert_string_to_binary(st):
    st = list(map(bin,bytearray(st,'ascii')))

    return st

def convert_binary_string_to_ascii(st):
    bi = chr(int(st,2))

    return bi

def establish_connection(dst, dport):

    mysocket = socket.socket()
    mysocket.connect((dst,dport))
    mystream = StreamSocket(mysocket)
    return mystream

def create_packet(src, dst, sport, dport): 

    # for creating packet: source ip, dst ip, sport, dport, seq, random data
    packet = IP(src=src, dst=dst)/TCP(sport=sport, dport=dport)/Raw()

    print("Packet summary:\t\t" + packet.summary() + " (Data: " + str(packet[TCP].load) + ")")

    return packet

def send_packet(packet):
    send(packet)

def toggle_psh(packet):
    if packet[TCP].flags== 8:
        packet[TCP].flags=""
    else:
        packet[TCP].flags="P"

    return packet

def encode_hash(st):
    
    # for hashing: source ip, dst ip, sport, dport, seq, random data
    params = str(st[IP].src) + " " + \
             str(st[IP].dst) + " " + \
             str(st[TCP].sport) + " " + \
             str(st[TCP].dport) + " " + \
             str(st[TCP].seq)

    #print("Parameters:\t\t", params) # this is currently spam

    result = sha256(str(params).encode())

    digest = result.hexdigest()

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
        print("Comparing " + binarydigest[arr[i]] + " and " + binarymessagestr[i] + "...")

        if binarydigest[arr[i]] == binarymessagestr[i]:
            print("The two bits match.")
            count += 1
        else:
            print("The two bits don't match.")
            break
    
    if count == 8:
        match = True

    return match

def compare_and_extract(binarydigest, permutation):

    binarydigeststr = str(binarydigest)
    binarystring = ""

    for i in range(0,len(permutation)):
        binarystring += binarydigest[permutation[i]]
        # print(binarystring)

    return binarystring

def compare_hex(st1, st2):
    return st1[-4:] == st2[-4:]

def generate_permutation_array(n=evalbits, k=256):
    permutation = []

    for i in range(0,n):
        redundancy = False # don't want repeating values in the permutation

        while not redundancy:
            index = randint(0,k-1)

            if index not in permutation:
                permutation.append(index)
                redundancy = True

    return permutation

## Code written by Xhonatan
## get the last 8 bits
def get_last_8bit(st):
    st = str(st)
    lastbits = st[-8:]
    return lastbits

## Code written by Xhonatan
def assemble(st1, st2):
    return st1 + st2
