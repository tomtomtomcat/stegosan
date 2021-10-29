from scapy.all import *

def incomming(pkt):
    # filters incomming packets on scource and destination
    # Or is just for testing
    if ((pkt[IP].src == scr) or (pkt[IP].dst == dst)):
        ## Example of what you see for summary
        ## IP / TCP 64.4.54.254:https > 192.168.1.78:33374 A / Padding
        print(pkt[IP].summary())
        ## Hex Packet Layout + Decoder
        ## https://hpd.gasmi.net/
        ## Notes for example Hex
        hexData = hexdump(pkt)
        print(hexData)

## dst scr are read as you are the sender
## This is how you get the source IP address
dst = get_if_addr(conf.iface)
print(dst)
scr = "127.0.0.1"
sniff(filter="ip", prn=incomming)




## NOTES!
## Old print out
# print(pkt[IP].payload)
## Revised version
# rawData = pkt.getlayer(Raw)
# print(rawData)
## Example Hex
## 142.250.190.42 → 192.168.1.78 TLSv1.2 Application Data 
## 2C D0 5A E4 09 53 38 3B C8 58 25 D5 08 00 45 00 00 66 8E 2F 00 00 3A 06 E3 47 8E FA BE 2A C0 A8 01 4E 01 BB 9F 8E 03 0C F7 F7 AA 21 7B CD 80 18 03 4B 75 C2 00 00 01 01 08 0A A4 BE D2 EC 82 8A 96 45 17 03 03 00 2D 5C 4F 74 47 43 A7 FF 67 6A BE E2 BD B6 9E FA 0F A5 24 50 E3 D5 6A 28 D0 9F EC 3E D9 DE F3 0D 24 06 7B 7F 45 B6 9F 51 F1 C6 FD 29 13 50