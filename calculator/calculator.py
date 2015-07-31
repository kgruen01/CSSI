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
import os
import jinja2





class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/calculator.html")
        self.response.write(template.render())

class MathHandler(webapp2.RequestHandler):
    def get(self):
        left = self.request.GET["left"]
        right = self.request.GET["right"]
        operation = self.request.get("operation")
        if operation == "add":
            self.response.write(float(left) + float(right))
        if operation == "subtract":
            self.response.write(float(left) - float(right))
        if operation == "multiply":
            self.response.write(float(left) * float(right))
        if operation == "divide":
            self.response.write(float(left) / float(right))
        if operation == "power":
            self.response.write(float(left) ** float(right))
        if operation == "sqrt":
            self.response.write(float(left) * math.sqrt(float(right)))
        if operation == "mod":
            self.response.write(float(left) % float(right))
        if operation == "sin":
            self.response.write(float(left) * math.sin(float(right)))
        if operation == "cos":
            self.response.write(float(left) * math.cos(float(right)))
        if operation == "tan":
            self.response.write(float(left) * math.tan(float(right)))
        if operation == "arcsin":
            self.response.write(float(left) * math.asin(float(right)))
        if operation == "arccos":
            self.response.write(float(left) * math.acos(float(right)))
        if operation == "arctan":
            self.response.write(float(left) * math.atan(float(right)))
        if operation == "ln":
            self.response.write(float(left) * math.log(float(right)))
        if operation == "log10":
            self.response.write(float(left) * math.log10(float(right)))
        if operation == "factorial":
            self.response.write(float(left) * math.factorial(float(right)))




jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/mathhandler', MathHandler)
], debug=True)
