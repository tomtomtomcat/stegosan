#!/usr/bin/python3
from scapy.all import *

# establish TCP connection
s = sys.argv[1]
d = sys.argv[2]
sport = random.randint(1024, 65535)
dport = int(sys.argv[3])

ip = IP(src=s, dst=d)
SYN = TCP(sport=sport, dport=dport, flags='S',seq=1000)
SYNACK = sr1(ip/SYN)

ACK = TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq+1)
send(ip/ACK)

# sniff on port
# sniff(filter= 'dst port 443')
