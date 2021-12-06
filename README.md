# stegosan

Linux: Requires python3-scapy (`sudo apt install python3-scapy`) and root (`sudo`) permissions to run

python version 3.8.10

```
usage: stegosan [-h] [-s | -r] [-src SRCIP] [-dst DSTIP] [-dport DSTPORT]

optional arguments:
  -h, --help            show this help message and exit
  -s, --send            Send packets
  -r, --receive         Receive packets
  -src SRCIP, --srcip SRCIP
                        Specify source IP
  -dst DSTIP, --dstip DSTIP
                        Specify destination IP
  -dport DSTPORT, --dstport DSTPORT
                        Specify destination port
 ```

Example command:
`sudo python3 main.py -src [srcip] -dst [dstip] -dport [dstport]`

Reference algorithm: 
Soni, Tapan, "Moving target network steganography" (2020). Theses and Dissertations. 2850. https://rdw.rowan.edu/etd/2850
