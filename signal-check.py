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

