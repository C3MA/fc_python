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

font = {"1":"""
#*#
**#
#*#
#*#
***""",
        "2":"""
***
##*
***
*##
***""",
        "3":"""
***
##*
***
##*
***""",
        "4":"""
*#*
*#*
***
##*
##*""",
        "5":"""
***
*##
***
##*
***""",
        "6":"""
***
*##
***
*#*
***""",
        "7":"""
***
##*
#*#
#*#
#*#""",
        "8":"""
***
*#*
***
*#*
***""",
        "9":"""
***
*#*
***
##*
***""",
        "0":"""
***
*#*
*#*
*#*
***""",
        ":":"""
###
#*#
###
#*#
###""",}


def getPixelForChar(char):

    c = font[char].strip()
  #  c = char.split("\n")
    ret = []

    y = 0
    x = 0

    for line in c:
        if line == "*":
            ret.append([x,y])
        if line == "\n":
            x=-1
            y+=1
        x+=1

    return ret



class ClockAni():

    frameCnt = 0

    dotColorR = 0x00
    dotColorG = 0x00
    dotColorB = 0xff

    dpOn = True

    def frameupdate(self,w,h):

        frame = FcFrame(w,h)

        h = time.strftime("%H")
        m = time.strftime("%M")

        zeile = 0
        spalte = 0

        for z in h:
            arrMap = getPixelForChar(z)
            for pix in arrMap:
                frame.setColorForPixel (spalte + pix[0], zeile+pix[1], self.dotColorR, self.dotColorG, self.dotColorB)
            spalte += 4

        zeile = 6
        spalte = 0

        for z in m:
            arrMap = getPixelForChar(z)
            for pix in arrMap:
                frame.setColorForPixel (spalte + pix[0], zeile+pix[1], self.dotColorR, self.dotColorG, self.dotColorB)
            spalte += 4

        self.frameCnt+=1

        if self.frameCnt > 253:
            return None

        if self.dotColorB >= 0x00 and self.dotColorR <= 0xff:
            self.dotColorB -= 2
            self.dotColorR += 2
        else:
            self.dotColorB = 0xff
            self.dotColorR = 0x00


        if (self.frameCnt % 30) == 0:
            self.dpOn = not self.dpOn

        if self.dpOn:
            punktOffsetX = w-3
            punktOffsetY = 3

            dp = getPixelForChar(':')

            for pix in dp:
                frame.setColorForPixel (punktOffsetX + pix[0], punktOffsetY+pix[1], 0x00, 0xff, 0x00)

        return frame.getProtobufPkt()

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
