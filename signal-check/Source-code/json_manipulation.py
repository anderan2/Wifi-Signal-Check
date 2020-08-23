import json


def write_to_json( signal, receive, transmit, path ):
	with open( path, 'w' ) as json_f:
		json_f.write( "Signal strengths (%):\t")
		json.dump( signal, json_f )
		json_f.write( "\n" )

		json_f.write( f"Receive rate (Mbps):\t")
		json.dump( receive, json_f )
		json_f.write( "\n" )

		json_f.write( f"Transmit rate (Mbps):\t")
		json.dump( transmit, json_f )