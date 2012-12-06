'''
Created on 05.12.2012

@author: ollo
'''

import socket
import sequence_pb2

PORT=24567

class FcClient(object):
    '''
    classdocs
    '''
    sock=0

    def __init__(self, targetip):
        '''
        Constructor
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((targetip, PORT))
        
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
        