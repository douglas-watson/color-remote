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

urls = (
        '/', 'index',
        '/foo', 'foo',
    )

render = web.template.render('templates/')
app = web.application(urls, globals())

colour_form = form.Form(
        form.Textbox("colour", description="Colour"),
        form.Button("submit", type="submit", description="Change colour")
    )

class index:
    def GET(self):
        f = colour_form()
        response = None
        return render.index(f, response)

    def POST(self):
        f = colour_form()
        if not f.validates():
            response = None
            return render.index(f, response)
        else:
            response = f.d.colour
            return render.index(f, response)

class foo:
    def GET(self):
        f = colour_form()
        return render.foo(f)


if __name__ == '__main__':
    app.run()
