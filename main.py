#!/usr/bin/python3

from args import *
from sender import *
from receiver import *

def main():
    if args.receive:
        receiver()
        # TODO finish receiver side
    elif args.send:
        sender()

if __name__ == "__main__":
    main()
