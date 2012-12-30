__author__ = 'bene'

#!/opt/local/bin/python2.7
#
# Some protobuf content for python:
# http://eigenein.info/protobuf/

from optparse import OptionParser
import sys
import socket
from PyFullcircle import FcClient, FcFrame, FcPixel
from PyFullcircleFonts import PyFcFonts


class RedDotAni():

    dotColorR = 0xff
    dotColorG = 0xff
    dotColorB = 0xff

    frameCnt = 0

    font1LineChars = {
        "$":"""
#*#*#*#*#*
#*##**#*##
#****#*##*
##***#**##
#***##****
#*#*##*#*#
##****#*#*
##**######
#*#***###*
##########
                  """
    }

    def __init__(self):
        self.fontObj = PyFcFonts(self.font1LineChars)

    def frameupdate(self, frame):
        self.frameCnt+=1

        self.fontObj.drawText(frame, 0, 0, "$", 0x48, 0x48, 0x48)

        if self.frameCnt > 60:
           return True

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target

    fps = 2
    width = 10
    height = 12

    rda = RedDotAni()

    try:
        client = FcClient(options.target)
        client.send_frames(fps, width, height, rda.frameupdate)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        parser.print_help()
        sys.exit(1)



if __name__ == "__main__":
    main()
