import argparse

parser = argparse.ArgumentParser(prog='stegosan')

group = parser.add_mutually_exclusive_group() # can only either send or receive
group.add_argument("-s", "--send", action="store_true", help="Send packets", default=True)
group.add_argument("-r", "--receive", action="store_true", help="Receive packets")
parser.add_argument("-src", "--srcip", type=str, help="Specify source IP")
parser.add_argument("-dst", "--dstip", type=str, help="Specify destination IP")
parser.add_argument("-sport", "--srcport", type=int, help="Specify source port")
parser.add_argument("-dport", "--dstport", type=int, help="Specify destination port")

args = parser.parse_args()


