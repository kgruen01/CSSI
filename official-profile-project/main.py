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
import os
import jinja2
import webapp2
# from google.appengine.ext import ndb

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             greeting = ('Welcome, %s! (<a href="%s">sign_out</a>)' %
#                 (user.nickname(), users.create_logout_url('/byebye')))
#         else:
#             greeting = ('<a href="%s">Sign in or register</a>.' %
#                 users.create_login_url('/'))
#         self.response.write('<html><body>%s</body></html>' % greeting)




# class ByeByeHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('<html><body>ByeBye</body></html>')



class MainHandler(webapp2.RequestHandler):
    def get(self):
        entry = jinja_environment.get_template("templates/index.html")
        self.response.write(entry.render(self.request.POST))


# class Words(ndb.Model):
#     this_is_the_message = ndb.StringProperty()

class MessageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Send me a message!")
        entry = jinja_environment.get_template("templates/message.html")
        self.response.write(entry.render(self.request.POST))

# class WordsHandler(webapp2.RequestHandler):


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/askbox', AskboxHandler)
], debug=True)
