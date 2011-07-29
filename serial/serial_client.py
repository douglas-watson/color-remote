#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   serial_client.py 
#
#   PURPOSE: connect to serial_server.py through twisted, to send colour change
#   requests
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
from twisted.python import util

"""
serial_client.py

connects to serial_driver.py, and enables colour changes. From the end-user
point of view, this module provides one function: set_colour(colour), that
looks after setting up a connection with the driver and requesting the colour
change.

"""

##############################
# Constants
##############################

HOSTNAME = 'localhost'
PORT = 54637

##############################
# Callbacks
##############################

def got_controller(obj, colour):
    # request the colour change
    # the return value of set_colour is success or not.
    return obj.callRemote("set_colour", colour)

def err_controller(reason):
    return "Failed to get RGB controller: " + reason

##############################
# Main loop
##############################

def set_colour(colour):
    # Setup connection with driver
    factory = pb.PBClientFactory()
    reactor.connectTCP(HOSTNAME, PORT, factory)
    # get RGBcontroller and request colour change
    d = factory.getRootObject() # get the RGB controller
    d.addCallback(got_controller, colour)
    d.addErrback(err_controller)
    # d.addCallback(util.println)
    d.addCallback(lambda _: reactor.stop()) # Exit immediately
    reactor.run()

if __name__ == '__main__':
    set_colour("#FF32II")
