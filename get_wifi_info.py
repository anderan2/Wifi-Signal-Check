def read_write_output(display, file_in, file_out ):
	with open( file_in, 'r' ) as read:
		lines = read.readlines()

	for line in lines:

		if "Transmit rate" in line:
			if line[ -3:-2 ] == ".":
				transmit = float( line[ -6:-1].strip() )
			else:
				if line[ -4:-3 ].rstrip() != ":":
					transmit = float( line[ -5: ].strip() )
				else:
					transmit = float( line[ -2: ].strip() )



		if "Receive rate" in line:
			if line[ -3:-2 ] == ".":
				receive = float( line[ -6: ].strip() )
				#receive_list += transmit
			else:
				if line[ -4:-3 ].rstrip() != ":":
					receive = float( line[ -5: ].strip() )
				else:
					receive = float( line[ -2: ].strip() )

			#print( receive )
		if "Signal" in line:
			strength = int( line[-5:-3].strip() )


	with open( file_out, 'a' ) as write:

		write.write( f"{display},{strength},{receive},{transmit}\n")
		write.close()

	return strength, receive, transmit







