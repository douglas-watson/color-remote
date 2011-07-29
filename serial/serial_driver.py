#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   serial_driver.py 
#
#   PURPOSE: Receive requests from serial_client.py and control the arduino in
#   response
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 29 July 2011
#
#   LICENSE: GNU GPL
#
#################################################

from twisted.spread import pb
from twisted.internet import reactor

##############################
# Constants 
##############################

HOSTNAME = 'localhost'
PORT = 54637

##############################
# Remotely callable stuff
##############################

class RGBController(pb.Root):
    def remote_set_colour(self, colour):
        print "Setting new colour:", colour
        with open("fake_serial", "a") as serial:
                serial.write("%s\n" % colour)
        return "success"

if __name__ == '__main__':
    reactor.listenTCP(PORT, pb.PBServerFactory(RGBController()))
    reactor.run()
