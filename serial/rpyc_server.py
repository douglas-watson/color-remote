#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   rpyc_server.py - an attempt using RPyC 
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 3rd August 2011
#
#   LICENSE: GNU GPL
#
#################################################

import rpyc
import serial

from constants import PORT, DEVICE

class RGBService(rpyc.Service):

    def on_connect(self):
        print "Connection received"

    def on_disconnect(self):
        print "Connection lost"

    def exposed_set_colour(self, colour):
        print "Colour request:", colour
        rgb = hex_to_rgb(colour)
        set_arduino_colour(rgb)
        # TODO replace this by logging call.
        with open('rpyc_serial', 'a') as fo:
            message = "%s %s %s" % rgb
            fo.write(message + "\n")
        return "Colour request %s transmitted to device." % colour

def hex_to_rgb(value):
    ''' Returns (red, green, blue) tuple of integers '''
    # by Jeremy Cantrell on stackoverflow
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def set_arduino_colour(rgb):
    ''' Asks the arduino via serial to set the colour according to values
    stored in rgb tuple '''
    # Arduino is running example code, that expects comma separated values,
    # such as: "150,240,10\n" for and RGB value of 150, 250, 10.
    
    arduino = serial.Serial(DEVICE)
    arduino.write("%d,%d,%d\n" % rgb)
    arduino.close()

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RGBService, port=PORT)
    t.start()
