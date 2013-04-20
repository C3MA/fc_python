__author__ = 'bene'

import alsaaudio, time, audioop
from optparse import OptionParser
import sys
import socket
from PyFullcircle import FcClient, FcFrame, FcPixel


class RedDotAni():

    dotPosY = 0
    dotColorR = 0x00
    dotColorG = 0x12
    dotColorB = 0x87
    snd = None

    def __init__(self, sound):
        self.snd = sound

    def frameupdate(self,frame):



        val = None
        l,data = self.snd.read()
        if l:
            val = round(audioop.max(data, 2) / 10)
        else:
            val = 0.0

        print val

        val = int(val) - 7

        print  (0, val, frame.getWidth() -1, val, self.dotColorR, self.dotColorG, self.dotColorB)

        frame.drawLine(0, val, frame.getWidth() -1, val, self.dotColorR, self.dotColorG, self.dotColorB)


        if self.dotPosY > frame.getHeight():
           return True



def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target

    fps = 10
    width = 7
    height = 10

    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(160)


    rda = RedDotAni(inp)

    try:
        client = FcClient(options.target)
        client.send_frames(fps, width, height, rda.frameupdate)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

