#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   rpyc_client.py - remotely call colour change requests 
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 3rd August 2011
#
#   LICENSE: GNU GPL
#
#################################################

import rpyc

from constants import HOST, PORT



def set_colour(colour):
    ''' All-in-one function to request a colour change '''
    connection = rpyc.connect(HOST, PORT)
    rgb_controller = connection.root
    return_value = rgb_controller.set_colour(colour)
    connection.close()
    return return_value

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print "Please supply a colour string as single argument"
        sys.exit(1)
    set_colour(sys.argv[1])
