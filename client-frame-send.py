#!/opt/local/bin/python2.7
#
# Some protobuf content for python:
# http://eigenein.info/protobuf/

from optparse import OptionParser
import sys
import socket
from PyFullcircle import FcClient

def frameupdate():
	print "we have to update a new frame and give it to the backend."

def main():
	usage = "usage: %prog [options] arg1 arg2"
	parser = OptionParser(usage=usage)	
	parser.add_option("-t", "--target",
                action="store", type="string", dest="target")
	(options, args) = parser.parse_args()
	print "Target"  , options.target
	
	try:
		client = FcClient(options.target)
		fps = 25
		width = 10
		height = 6
		client.send_frames(fps, width, height, frameupdate)		
	except socket.error, msg:
		sys.stderr.write("[ERROR] %s\n" % msg[1])
		parser.print_help()
		sys.exit(1)
		
	

if __name__ == "__main__":
    main()
