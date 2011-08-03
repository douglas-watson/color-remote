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

from constants import HOST, PORT, SUCCESS

class RGBClient(LineReceiver):

    def connectionMade(self):
        print "Connection established"
        self.sendLine(self.factory.colour)
        print "Line sent..."

    def lineReceived(self, line):
        if line == SUCCESS:
            print "...and successfully transmitted"
        self.transport.loseConnection()



class RGBClientFactory(ClientFactory):
    ''' Taylor made factory for each colour request. Takes a single string as
    argument, in the form of a hex colour value '''
    protocol = RGBClient

    def __init__(self, colour):
        self.colour = colour.encode('ascii', 'replace')

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed:', reason.getErrorMessage()
        # make sure the reactor is stopped
        if reactor.running:
            reactor.stop()
        sys.exit(1)

    def clientConnectionLost(self, connector, reason):
        print 'Connection lost:', reason.getErrorMessage()
        # make sure reactor is stopped
        if reactor.running:
            reactor.stop()

def set_colour(colour):
    # f = RGBClientFactory(colour)
    f = RGBClientFactory(colour)
    reactor.connectTCP(HOST, PORT, f)
    if not reactor.running:
        reactor.run()

if __name__ == '__main__':
    # just test a colour change request
    set_colour(sys.argv[1])
