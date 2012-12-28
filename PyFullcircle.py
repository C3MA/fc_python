'''
Created on 05.12.2012

@author: ollo
'''

import socket
import sequence_pb2

CLIENT_COLOR="red"
SEQUENCE_ID=1
GENERATOR_NAME="pyClient1"
GENERATOR_VERSION="0.1"

PORT=24567

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
        
        # read from the socket (expect Pong)
        rawreceive = self.sock.recv(10)
        # extract length of header (simply the first 10 bytes)
        length = (rawreceive[:10]).strip()
        print ("Got %s bytes" % length) # FIXME remove debug line
        
        # read protobuf content
        content = self.sock.recv(int(length))
        incoming = sequence_pb2.Snip.FromString( content )
        
        # type has to be looked up manually from the sequence.proto
        if (incoming.type == 5):
            return incoming.pong_snip.count
        else:
            raise socket.error("custom", "Wrong type, expected PongSnip" )
    
        