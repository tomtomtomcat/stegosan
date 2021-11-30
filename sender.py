from args import *
from config import *
from helper import *

def sender():

    src = args.srcip
    dst = args.dstip
    sport = random.randint(1024, 65535)
    seq = random.randint(1024, 65535)
    dport = args.dstport

    # TODO test and use for final debugging
    mystream = establish_connection(src,dst,sport,dport)

    cont = True

    while cont: # until user stops sending messages
        message = take_input()
        print("Message:\t\t", message)

        binarymessage = convert_string_to_binary(message) # get binary representation
        print("Binary representation:\t", binarymessage)

        random.seed(secretkey) # use preshared seed for permutation generator
        permutation = generate_permutation_array()
        print("Permutation array:\t", permutation)

        packetcounter = 0
        messagecounter = 0

        for i in binarymessage:
            match = False

            fmessage = format_input(message, messagecounter)
            messagecounter += 1
            print(fmessage)

            while not match: 
                packet = create_packet(src, dst, sport, dport, seq)
                packetcounter += 1

                packet = toggle_psh(packet) 
 
                digest = encode_hash(packet)
                print("Packet hash digest:\t", digest)

                binarydigest = convert_hex_to_binary(digest)

                if compare_bits_with_arr(i, binarydigest, permutation):
                    mystream.send(packet)
                    print("Match! Sending marked packet representing \"" \
                    + convert_binary_string_to_ascii(i) + "\".\n")
                    match = True
                else:
                    packet = toggle_psh(packet) 
 
                    mystream.send(packet)
                    print("No match. Sending unmarked packet.\n")

        print("Fully sent message: \"" + message + "\".")
        print("Total packets sent:", packetcounter)
        print("\nWant to send additional messages?: (y/n)")

        choice = input()
        if (choice != 'y'):
	        cont = False
	        print("\nClosing connection.")
