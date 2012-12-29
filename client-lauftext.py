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

    dotPosX = 10
    dotPosY = 0
    dotColorR = 0xef
    dotColorG = 0x30
    dotColorB = 0x10

    #text = "C3MA - CHAOS IM QUADRAT"

    text = "SEXIEST ERFA 2012 - SEXIEST ERFA 2012 - SEXIEST ERFA 2012 - SEXIEST ERFA 2012 - SEXIEST ERFA 2012"

   # text = "29C3 - NOT MY DEPARTMENT"

    frameCnt = 0

    def __init__(self):
        self.fontObj = PyFcFonts(PyFcFonts.font2LineChars)

    def frameupdate(self,w,h):
        self.frameCnt+=1
        frame = FcFrame(w,h)

        for x in range(0,w):
            for y in range(0,h):
                frame.setColorForPixel(x,y,0x88,0x88,0x88)



        self.fontObj.drawText(frame, self.dotPosX, 1, self.text, self.dotColorR, self.dotColorG, self.dotColorB)

    #    if self.frameCnt > 253:
    #       return None

        if (self.frameCnt % 1) == 0:
            self.dotPosX -= 1

        if self.dotPosX < (len(self.text)+1)*-5:
            return None

        return frame.getProtobufPkt()

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target

    fps = 6
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
