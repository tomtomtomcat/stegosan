#!/usr/bin/python3

import argparse
import configparser

from sender import *
from receiver import *

def main():
    # read config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    evalbits = config['preshared']['EvaluationBits']
    secretkey = config['preshared']['SecretKey']
    retries =  config['preshared']['RetryCount']
    
    # parse arguments
    parser = argparse.ArgumentParser(prog='stegosan')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--send", action="store_true", help="Send packets", default=True)
    group.add_argument("-r", "--receive", action="store_true", help="Receive packets")
    parser.add_argument("-src", "--srcip", type=str, help="Specify source IP")
    parser.add_argument("-dst", "--dstip", type=str, help="Specify destination IP")
    parser.add_argument("-dport", "--dstport", type=int, help="Specify destination port")
    
    args = parser.parse_args()

    if args.receive:
        receiver(args, evalbits, secretkey, retries)
        # TODO finish receiver side
    elif args.send:
        sender(args, evalbits, secretkey, retries)

if __name__ == "__main__":
    main()
