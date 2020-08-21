import time
import os
import json
from get_wifi_info import read_write_output

"""******************************************************************
Author: 			Andrew A. Anderson
Date Made:			8/20/2020
Date Mod:			8/21/2020
Release:			V1.2.0

Purpose:			I built this programme because I got annoyed with
					my ISP saying that there was nothing wrong on
					their end for my internet speed.

					In order to use this, save signal-check.py on
					your desktop.

					Create a folder called "python_work" on your
					desktop. Then run signal-check.py


Modifications:		Improved directory structure for clarity, also
					added in json output.

If you run into any issues, please contact me via github.
******************************************************************"""


json_file_path = '../Json-file/json_file.json'

signal_list = []
transmit_list = []
receive_list = []


x = 1
file_name = '../CSV-file/signal_output.csv'

read_file = '../Input-file/interface.txt'

with open( file_name, 'a' ) as f:
	f.write( "Time (HH:MM:SS),Signal (%),Receive (Mbps),Transmit (Mbps)\n")
	f.close()



while x <= 5:
	local = time.localtime()
	display = time.strftime( "%I:%M:%S %p", local )
	os.system( "netsh wlan show interfaces > ../Input-file/interface.txt" )
	strength, receive, transmit = read_write_output( display, read_file, file_name )
	time.sleep( 1 )
	x += 1
	signal_list.append( strength )
	receive_list.append( receive )
	transmit_list.append( transmit )




with open( json_file_path, 'a' ) as json_f:
	json_f.write( "Signal strengths (%):\t")
	json.dump( signal_list, json_f )
	json_f.write( "\n" )

	json_f.write( f"Receive rate (Mbps):\t")
	json.dump( receive_list, json_f )
	json_f.write( "\n" )

	json_f.write( f"Transmit rate (Mbps):\t")
	json.dump( transmit_list, json_f )


