__author__ = 'bene'

import alsaaudio, time, audioop
from optparse import OptionParser
import sys
import socket
import threading
from PyFullcircle import FcClient, FcFrame, FcPixel


class AudioThread(threading.Thread):
    audioInput = None

    def __init__(self):
        threading.Thread.__init__(self)

        self.audioInput = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

        # Das sind alles Default werte!
        #inp.setchannels(2)
        #inp.setrate(44100)
        #in.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        #inp.setperiodsize(32)


    def run(self):
        while 1:
            self.audioInput.read()

    def getData(self):
        return self.audioInput.read()


class RedDotAni():

    dotPosY = 0
    dotColorR = 0x00
    dotColorG = 0x12
    dotColorB = 0x87
    snd = None

    def __init__(self):
        self.snd = AudioThread()
        self.snd.start()

    def frameupdate(self,frame):

        val = None
        l,data = self.snd.getData()
        if l:
            val = round(audioop.max(data, 4))
        else:
            val = 0.0

        print val

        val = int(val)

        print  (0, frame.getHeight() - val, frame.getWidth() -1, frame.getHeight() - val, self.dotColorR, self.dotColorG, self.dotColorB)

        if self.dotPosY > frame.getHeight():
           return True

        frame.drawLine(0, frame.getHeight() - val, frame.getWidth() -1, frame.getHeight() - val, self.dotColorR, self.dotColorG, self.dotColorB)


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target",
        action="store", type="string", dest="target")
    (options, args) = parser.parse_args()
    print "Target"  , options.target



    snd = AudioThread()
    snd.start()

    print "Thread OK!"

    val = None
    while 1:

        l,data = snd.getData()
        if l:
            val = round(audioop.max(data, 4))
        else:
            continue;


        print val % 100


    exit(1)

    fps = 60
    width = 7
    height = 10

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

