def read_write_output(display, file_in, file_out ):
	with open( file_in, 'r' ) as read:
		lines = read.readlines()

	for line in lines:

		if "Transmit rate" in line:
			if line[ -3:-2 ] == ".":
				transmit = line[ -6:-1].strip()
				#print( transmit )
			else:
				if line[ -4:-3 ].rstrip() != ":":
					transmit = line[ -5: ].strip()
					#print( transmit )
				else:
					transmit = line[ -2: ].strip()
					#print( transmit )


		if "Receive rate" in line:
			if line[ -3:-2 ] == ".":
				receive = line[ -6: ].strip()
			else:
				if line[ -4:-3 ].rstrip() != ":":
					receive = line[ -5: ].strip()
				else:
					receive = line[ -2: ].strip()
			#print( receive )
		if "Signal" in line:
			strength = line[-5:-3].strip()

	with open( file_out, 'a' ) as write:

		write.write( f"{display},{strength},{receive},{transmit}\n")
		write.close()