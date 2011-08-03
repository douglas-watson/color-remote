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

from constants import PORT

class RGBService(rpyc.Service):

    def on_connect(self):
        print "Connection received"

    def on_disconnect(self):
        print "Connection lost"

    def exposed_set_colour(self, colour):
        print "Colour request:", colour
        with open('rpyc_serial', 'a') as fo:
            fo.write(colour + "\n")

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RGBService, port=PORT)
    t.start()
