import time
import os
import json
from json_manipulation import write_to_json
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

runtime_length = input( "How many seconds do you want the program to run?\n>> " )

running = int( runtime_length )

x = 1


file_name = '../CSV-file/signal_output.csv'

read_file = '../Input-file/interface.txt'

with open( file_name, 'a' ) as f:
	f.write( "Time (HH:MM:SS),Signal (%),Receive (Mbps),Transmit (Mbps)\n")
	f.close()


print( f"Running for {running} seconds: \n", flush = True)
time.sleep( 1 )
while running >= x:
	local = time.localtime()
	display = time.strftime( "%I:%M:%S %p", local )
	os.system( "netsh wlan show interfaces > ../Input-file/interface.txt" )
	""" retrieve the signal strength, transmit rate, and receive rate from your Wifi """
	strength, receive, transmit = read_write_output( display, read_file, file_name )
	time.sleep( 1 )
	running = running - 1
	signal_list.append( strength )
	receive_list.append( receive )
	transmit_list.append( transmit )
	if running % 5 == 0 and running != 0:
		print( f"\t{running} seconds remaining", flush = True)

print( "\nsignal_output.csv created.", flush = True )
time.sleep( 3 )


print( "\nSaving to json_file.json....", flush = True )
time.sleep( 3 )
write_to_json( signal_list, receive_list, transmit_list, json_file_path)
print( "\nSaved to json_file.json.\n\nGoodbye.", flush = True )


