from datetime import date

__author__ = 'bene'

#!/opt/local/bin/python2.7
#
# Some protobuf content for python:
# http://eigenein.info/protobuf/

from optparse import OptionParser
import sys
import socket
from PyFullcircle import FcClient, FcFrame, FcPixel
import time
from PyFullcircleFonts import PyFcFonts

class ClockAni():

    frameCnt = 0

    dotColorR = 0x00
    dotColorG = 0x00
    dotColorB = 0xff

    dpOn = True

    def __init__(self):
        self.fontObj = PyFcFonts(PyFcFonts.font2LineNumbers)

    def frameupdate(self, frame):

        h = time.strftime("%H")
        m = time.strftime("%M")

        self.fontObj.drawText(frame, 0,0, h +"\n"+ m , self.dotColorR, 0x00, self.dotColorB)

        self.frameCnt+=1

        if self.frameCnt > 253:
            return True

        if self.dotColorB >= 0x00 and self.dotColorR <= 0xff:
            self.dotColorB -= 2
            self.dotColorR += 2
        else:
            self.dotColorB = 0xff
            self.dotColorR = 0x00


        if (self.frameCnt % 30) == 0:
            self.dpOn = not self.dpOn

        if self.dpOn:

            self.fontObj.drawText(frame, frame.getWidth() -3,3, ":" , 0x00, 0xff, 0x00)


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target

    fps = 30
    width = 10
    height = 12

    rda = ClockAni()

    try:
        client = FcClient(options.target)
        client.send_frames(fps, width, height, rda.frameupdate)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        parser.print_help()
        sys.exit(1)



if __name__ == "__main__":
    main()
