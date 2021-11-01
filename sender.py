from helper import *

def sender():
    message = take_input()

    src = sys.argv[2]
    dst = sys.argv[3]
    sport = random.randint(1024, 65535)
    dport = int(sys.argv[4])

    # TODO test and use for final debugging
    # establish_connection()

    cont = True
    while cont: # until user stops wanting to send messages
        binarymessage = convert_to_binary(message)

        packet = create_packet(src, dst, sport, dport)

        digest = encode_hash(packet, message)

        binarydigest = convert_to_binary(digest)
        
        # match = TODO compare_bits(binarymessage, binarydigest)
        # if match:
        #     send_packet(packet) # TODO
        # else:
        #     packet = remove_flag(packet) # TODO 
        #     send_packet(packet)

        print("Want to send additional messages?: (y/n)")

        choice = input()
        if (choice != 'y'):
	        cont = False
	        # TODO close_connection()
        else:
	        message = take_input()
