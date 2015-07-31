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
import logging
import os
import jinja2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Hello world")
        template = jinja_environment.get_template("templates/are-you-pretty.html")
        self.response.write(template.render())


class NameHandler(webapp2.RequestHandler):
    def get(self):
        response = jinja_environment.get_template("templates/are-you-pretty-response.html")
        self.response.write(response.render())
        name = self.request.get("name", default_value="Friend")
        self.response.write(name + ", you are very pretty! Have a wonderful day.")


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/NameHandler', NameHandler)
], debug=True)
