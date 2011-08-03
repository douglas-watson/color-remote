#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   serial_driver.py - Simpler attempt at the colour changer daemon 
#
#   PURPOSE: Receive colour change requests from serial_client.py and relay
#   them to an Arduino connected to an RGB LED
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 2nd August 2011
#
#   LICENSE: GNU GPL
#
#################################################

from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor

from constants import HOST, PORT, SUCCESS


# This is just about the simplest possible protocol
class RGBControl(LineReceiver):

    def connectionMade(self):
        print "Connection received from", self.transport.client
        # keep track of connected clients

    def lineReceived(self, line):
        """ Receive a single line containing the hex colour code """
        print "Received line:", line
        self.sendLine(SUCCESS)

        # for the moment, just write to fake_serial
        with open('fake_serial', 'a') as fo:
            fo.write(line + "\n") # line does not contain end of line char.

    def connectionLost(self, reason):
        print "Connection lost:", reason.getErrorMessage()


def main():
    f = Factory()
    f.protocol = RGBControl
    f.numProtocols = 0
    reactor.listenTCP(PORT, f)
    if not reactor.running:
        reactor.run()

if __name__ == '__main__':
    main()
