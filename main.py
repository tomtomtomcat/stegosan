#!/usr/bin/python3

import hashlib

from sender import *
from receiver import *

def main():
    if sys.argv[1] == "s":
        sender()
    else:
        receiver()
        # TODO finish receiver side

main()
