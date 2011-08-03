#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
#   request_handler.py - Serves pages and handles requests for colour changes 
#
#   AUTHOR: Douglas Watson <douglas@watsons.ch>
#
#   DATE: started on 12 July 2011
#
#   LICENSE: GNU GPL
#
#################################################

import web
from web import form

import sys
sys.path.append('../serial')
from constants import HOST, PORT
import rpyc_client


urls = (
        '/', 'index',
        '/foo', 'foo',
    )

render = web.template.render('templates/')
app = web.application(urls, globals())

colour_form = form.Form(
        form.Textbox("colour",
            form.notnull,
            form.regexp(r'^#[a-fA-F0-9]{3}|[a-fA-F0-9]{6}$', 
                'Invalid colour code'),
            description="Pick a colour!", id='colour',
            value="#a5ed82"),
        form.Button("submit", type="submit", html="Set colour!", 
            description="Change colour")
    )

class index:
    def GET(self):
        f = colour_form()
        response = None
        return render.index(f, response)

    def POST(self):
        f = colour_form()
        if not f.validates():
            response = 'Invalid input'
            return str(response)
        else:
            # Adapted for ajax, return only response string, not template.
            colour = f['colour'].value
            # Write to log file
            with open("log", 'a') as fo:
                fo.write(str(colour) + "\n")
            # Request colour change through serial driver
            return_value = rpyc_client.set_colour(colour)
            return return_value
if __name__ == '__main__':
    app.run()
