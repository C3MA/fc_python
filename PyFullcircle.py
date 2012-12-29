'''
Created on 05.12.2012

@author: ollo
'''

import socket
import sequence_pb2
import time
import threading

CLIENT_COLOR="red"
SEQUENCE_ID=1
GENERATOR_NAME="pyClient1"
GENERATOR_VERSION="0.1"

PORT=24567

class FcPixel():
    red = None
    green = None
    blue = None

    def __init__(self, r,g,b):
        self.red = r
        self.green = g
        self.blue = b

    def setColor(self, r,g,b):
        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        return "r%sg%sb%s" % (self.red, self.green, self.blue)


def getEOS():

    payload = sequence_pb2.Snip()
    # payload.eos_snip
    # type has to be looked up manually from the sequence.proto
    payload.type = 11

    return payload.SerializeToString()

class FcFrame():
    width = None
    height = None

    pixels = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []


        tmpArr = []

        for x in range( 0,width):
            for y in range( 0,height):
                tmpArr.append(FcPixel(0,0,0))
            self.pixels.append(tmpArr)
            tmpArr = []


    def __str__(self):
        str = ""
        for x in range( 0,self.width):
            for y in range( 0,self.height):
                str += ";%s" % self.pixels[x][y]

        return "Frame: " + str

    def setColorForPixel(self, x,y,r,g,b):

        if x >= self.width or y >= self.height:
            return

        if r > 255 or g > 255 or b > 255 or r < 0 or g  < 0 or b < 0:
            return

        self.pixels[x][y].setColor(r,g,b)

        if x >= self.width or y >= self.height:
            return

        if r > 255 or g > 255 or b > 255 or r < 0 or g  < 0 or b < 0:
            return

        self.pixels[x][y].setColor(r,g,b)

    def drawLine(self, x1, y1, x2, y2, red, green, blue):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.setColorForPixel(x, y, red, green, blue)
                
    def getProtobufPkt(self):

        payload = sequence_pb2.Snip()

        for x in range( 0,self.width):
            for y in range( 0,self.height):
                pix = payload.frame_snip.frame.pixel.add()
                pix.x = x
                pix.y = y
                pix.blue = self.pixels[x][y].blue
                pix.green = self.pixels[x][y].green
                pix.red = self.pixels[x][y].red

        payload.type = 6

        return payload.SerializeToString()

class FcClient(object):
    '''
    classdocs
    '''
    sock=0

    def __init__(self, targetIP):
        '''
        Constructor
        '''
        if (targetIP is None):
            raise socket.error("custom", "No target IP specified" )
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((targetIP, PORT))
        
    def ping(self, count):
        # Build the snippet
        payload = sequence_pb2.Snip()
        payload.ping_snip.count = count
        # type has to be looked up manually from the sequence.proto
        payload.type = 1
        
        # send protobuf-package; put a header of 10 bytes in front 
        # with the length of the content (as ASCII and aligend to the "right")
        raw2send = payload.SerializeToString()
        head = '%10d' % len(raw2send)
        self.sock.send(head + raw2send)
        
        # read from the socket (expect Pong)
        rawreceive = self.sock.recv(10)
        # extract length of header (simply the first 10 bytes)
        length = (rawreceive[:10]).strip()
        
        # read protobuf content
        content = self.sock.recv(int(length))
        incoming = sequence_pb2.Snip.FromString( content )
        # type has to be looked up manually from the sequence.proto
        if (incoming.type == 2):
            return incoming.pong_snip.count
        else:
            raise socket.error("custom", "Wrong type, expected PongSnip" )
        
    def send_frames(self, fps, width, height, frameupdate):

        self.callBack = frameupdate
        self.w = width
        self.h = height

        #FIXME test blubb
        self.sleepTime = (1.0 / fps)
        print("wait %f s between two frames" % self.sleepTime)
        
        # Build the snippet
        payload = sequence_pb2.Snip()
        payload.req_snip.color = CLIENT_COLOR
        payload.req_snip.seqId = SEQUENCE_ID
        payload.req_snip.meta.frames_per_second = fps
        payload.req_snip.meta.width = width
        payload.req_snip.meta.height = height
        payload.req_snip.meta.generator_name = GENERATOR_NAME
        payload.req_snip.meta.generator_version = GENERATOR_VERSION
        # type has to be looked up manually from the sequence.proto
        payload.type = 4
        
        # send protobuf-package; put a header of 10 bytes in front 
        # with the length of the content (as ASCII and aligend to the "right")
        raw2send = payload.SerializeToString()
        head = '%10d' % len(raw2send)
        self.sock.send(head + raw2send)
        print("Sent the request") # FIXME remove debug line
        
        # read from the socket (expect Ack)
        rawreceive = self.sock.recv(10)
        # extract length of header (simply the first 10 bytes)
        length = (rawreceive[:10]).strip()
        #print ("Got %s bytes" % length) # FIXME remove debug line
        
        # read protobuf content
        content = self.sock.recv(int(length))
        incoming = sequence_pb2.Snip.FromString( content )


        # wait for ack
        if (incoming.type == 7):
            print ("Starting endless loop, we can SEND something")

            self.br = False
            self.cont = ""
            self.sendPossible = False

            self.timerSend()

        else:
            raise socket.error("custom", "Wrong type, expected Ack" )

    def timerSend(self):

        print "Timer Call!"


        if (not self.sendPossible):
            # read from the socket (expect Ack)
            rawreceive = self.sock.recv(10)
            # extract length of header (simply the first 10 bytes)
            length = (rawreceive[:10]).strip()

            print ("Got %s bytes" % length) # FIXME remove debug line

            # read protobuf content
            content = self.sock.recv(int(length))
            incoming = sequence_pb2.Snip.FromString( content )

            print ("Got type %d " %  incoming.type)

            if (incoming.type == 5):
                self.sendPossible = True

        if (self.sendPossible):

            try:
                cont = self.callBack(self.w, self.h)
            except Exception as ext:
                print "Da isn Fehler!"
                print ext.message
                cont = None

            if cont is None:
                cont = getEOS()
                self.br = True
            head = '%10d' % len(cont)
            self.sock.send(head + cont)
            if self.br:
                print ("Peace Off!")
                return

        if not self.br:
            threading.Timer(self.sleepTime, self.timerSend).start()

