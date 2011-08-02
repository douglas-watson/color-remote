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

HOST = 'localhost'
PORT = 54636

# This is just about the simplest possible protocol
class RGBControl(LineReceiver):

    def connectionMade(self):
        print "Connection received from", self.transport.client

    def lineReceived(self, line):
        """ Receive a single line containing the hex colour code """
        print "Received line:", line
        # for the moment, just write to fake_serial
        self.transport.loseConnection()
        with open('fake_serial', 'a') as fo:
            fo.write(line + "\n") # line does not contain end of line char.


def main():
    f = Factory()
    f.protocol = RGBControl
    reactor.listenTCP(PORT, f)
    reactor.run()

if __name__ == '__main__':
    main()
