#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import math
import logging
import jinja2
import os



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {"timeofday": time.asctime()}
        template = jinja_environment.get_template("templates/calculator.html")
        self.response.write(template.render(template_vars))

class FormHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("name")
        self.response.write("It worked! Name entered is: " + name)


class AddHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("+")
        self.response.write(right)
        self.response.write("=")
        self.response.write(float(left) + float(right))

class SubtractHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("-")
        self.response.write(right)
        self.response.write("=")
        self.response.write(float(left) - float(right))

class MultiplyHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("*")
        self.response.write(right)
        self.response.write("=")
        self.response.write(int(left) * int(right))

class DivideHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("/")
        self.response.write(right)
        self.response.write("=")
        self.response.write(int(left) / int(right))

class PowerHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("^")
        self.response.write(right)
        self.response.write("=")
        self.response.write(int(left) ** int(right))

class ModHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("%")
        self.response.write(right)
        self.response.write("=")
        self.response.write(int(left)%int(right))

class SineHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("sin(")
        self.response.write(right)
        self.response.write(")")
        self.response.write("=")
        self.response.write(int(left) * math.sin(int(right)))

class CosineHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        self.response.write(left)
        self.response.write("cos(")
        self.response.write(right)
        self.response.write(")")
        self.response.write("=")
        self.response.write(int(left) * math.cos(int(right)))


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/subtract', SubtractHandler),
    ('/multiply', MultiplyHandler),
    ('/divide', DivideHandler),
    ('/power', PowerHandler),
    ('/mod', ModHandler),
    ('/sine', SineHandler),
    ('/cosine', CosineHandler),
    ('/formhandler', FormHandler)
], debug=True)
