from helper import *

def sender(args):
    message = take_input()

    src = args.srcip
    dst = args.dstip
    sport = random.randint(1024, 65535)
    dport = args.dstport

    # TODO test and use for final debugging
    # establish_connection()

    cont = True

    while cont: # until user stops wanting to send messages
        
        messagefullysent = False # TODO not fully functional

        while not messagefullysent:
            binarymessage = convert_to_binary(message)

            packet = create_packet(src, dst, sport, dport)

            packet = toggle_psh(packet) 

            digest = encode_hash(packet, message)

            binarydigest = convert_to_binary(digest)
            
            match = compare_bits(binarymessage, binarydigest)

            if match:
                # send_packet(packet) # TODO
                print("Match")
            else:
                # packet = toggle_psh(packet) # TODO 
                # send_packet(packet)
                print("No match")

            messagefullysent = True

        print("Want to send additional messages?: (y/n)")

        choice = input()
        if (choice != 'y'):
	        cont = False
	        # TODO close_connection()
        else:
	        message = take_input()
