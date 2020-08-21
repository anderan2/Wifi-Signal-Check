import time
import os
import json
from get_wifi_info import read_write_output

"""******************************************************************
Author: 			Andrew A. Anderson
Date Made:			8/20/2020
Date Mod:			8/20/2020
Release:			V1.1.0

Purpose:			I built this programme because I got annoyed with
					my ISP saying that there was nothing wrong on
					their end for my internet speed.

					In order to use this, save signal-check.py on
					your desktop.

					Create a folder called "python_work" on your
					desktop. Then run signal-check.py


Modifications:		Made the read_write_output function for
					readability. 

If you run into any issues, please contact me via github.
******************************************************************"""

#def read_write_output(display, file_in, file_out ):
#	with open( file_in, 'r' ) as read:
#		lines = read.readlines()

#	for line in lines:

#		if "Transmit rate" in line:
#			if line[ -3:-2 ] == ".":
#				transmit = line[ -6:-1].strip()
#				#print( transmit )
#			else:
#				if line[ -4:-3 ].rstrip() != ":":
#					transmit = line[ -5: ].strip()
#					#print( transmit )
#				else:
#					transmit = line[ -2: ].strip()
#					#print( transmit )


#		if "Receive rate" in line:
#			if line[ -3:-2 ] == ".":
#				receive = line[ -6: ].strip()
#			else:
#				if line[ -4:-3 ].rstrip() != ":":
#					receive = line[ -5: ].strip()
#				else:
#					receive = line[ -2: ].strip()
			#print( receive )
#		if "Signal" in line:
#			strength = line[-5:-3].strip()

#	with open( file_out, 'a' ) as write:

#		write.write( f"{display},{strength},{receive},{transmit}\n")
#		write.close()




x = 1
file_name = './python_work/signal_output.csv'

read_file = './python_work/output.txt'

with open( file_name, 'a' ) as f:
	f.write( "Time (HH:MM:SS),Signal (%),Receive (Mbps),Transmit (Mbps)\n")
	f.close()



while x < 900:
	local = time.localtime()
	display = time.strftime( "%I:%M:%S %p", local )
	os.system( "netsh wlan show interfaces > ./python_work/output.txt" )
	read_write_output( display, read_file, file_name )
	time.sleep( 2 )
	x += 1

