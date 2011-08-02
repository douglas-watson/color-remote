#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   serial_client.py - a simpler attempt
#
#   PURPOSE: Send colour change requests to the serial driver. 
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 2nd August 2011
#
#   LICENSE: GNU GPL
#
#################################################

import sys

from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ClientFactory
from twisted.internet import reactor

HOST = 'localhost'
PORT = 54636

class RGBClient(LineReceiver):
    def connectionMade(self):
        print "Connection established"
        # change colour
        # self.sendLine(self.factory.colour)
        self.sendLine("FF33JX")
        print "Line sent"



class RGBClientFactory(ClientFactory):
    ''' Taylor made factory for each colour request. Takes a single string as
    argument, in the form of a hex colour value '''
    protocol = RGBClient

    # def __init__(self, colour):
        # self.colour = colour.decode('ascii', 'replace')

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed:', reason.getErrorMessage()
        # make sure the reactor is stopped
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'Connection lost:', reason.getErrorMessage()
        # make sure reactor is stopped
        reactor.stop()

def set_colour(colour):
    # f = RGBClientFactory(colour)
    f = RGBClientFactory()
    reactor.connectTCP(HOST, PORT, f)
    reactor.run()

if __name__ == '__main__':
    # just test a colour change request
    set_colour("FF33JX")
