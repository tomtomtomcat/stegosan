from helper import *

def sender(args, evalbits, secretkey, retries):

    src = args.srcip
    dst = args.dstip
    sport = random.randint(1024, 65535)
    seq = random.randint(1024, 65535)
    dport = args.dstport

    # TODO test and use for final debugging
    # establish_connection(src,dst,sport,dport)

    cont = True

    while cont: # until user stops wanting to send messages
        message = take_input()

        binarymessage = convert_string_to_binary(message)
        random.seed(secretkey)
        arr = permu()

        packetcounter = 0

        for i in binarymessage:
            match = False
            while not match: 
                packet = create_packet(src, dst, sport, dport, seq)
                packetcounter += 1

                packet = toggle_psh(packet) 

                digest = encode_hash(packet)

                binarydigest = convert_hex_to_binary(digest)

                if compare_bits_with_arr(i, binarydigest, arr):
                    # send_packet(packet) # TODO
                    print("Match! Sending marked packet representing \"" \
                    + convert_binary_string_to_ascii(i) + "\".\n")
                    match = True
                else:
                    packet = toggle_psh(packet) 
                    # send_packet(packet)
                    print("No match. Sending unmarked packet.\n")

 
	
        print("Fully sent message: \"" + message + "\".")
        print("Total packets sent:", packetcounter)
        print("Want to send additional messages?: (y/n)")

        choice = input()
        if (choice != 'y'):
	        cont = False
	        print("\nClosing connection.")
	        # TODO close_connection()
