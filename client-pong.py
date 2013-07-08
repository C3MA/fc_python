__author__ = 'bene'

#!/opt/local/bin/python2.7
#
# Some protobuf content for python:
# http://eigenein.info/protobuf/

from optparse import OptionParser
import sys
import socket
from PyFullcircle import FcClient, FcFrame, FcPixel


class Pong():

    ballX = 3
    ballY = 3
    ballDirX = 1
    ballDirY = 1

    frameCnt = 0

    def frameupdate(self,frame):
        frameCnt += 1
        if frameCnt > 200:
            return True
        
        ballX += ballDirX
        ballY += ballDirY


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target

    fps = 10
    width = 10
    height = 12

    p = Pong()

    try:
        client = FcClient(options.target)
        client.send_frames(fps, width, height, p.frameupdate)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        parser.print_help()
        sys.exit(1)



if __name__ == "__main__":
    main()
