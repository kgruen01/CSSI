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
import jinja2
import urllib2
import json
import os
import logging
import datetime
from google.appengine.ext import ndb

class Temperature(ndb.Model):
    temperature = ndb.FloatProperty()
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    created = ndb.DateTimeProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        temp = Temperature(temperature=75, latitude=46, longitude=-122, created=datetime.datetime.now())
        temp.put()
        # query = User.query()
        # data = query.fetch()
        # logging.info(data)


class TemperatureHandler(webapp2.RequestHandler):
    def get(self):
        #loading in template file
        template = jinja_environment.get_template("templates/index.html")
        #Get lat and lon from javascript
        lat = self.request.get("lat")
        lon = self.request.get("lon")
        #creating url for API request
        url = ("http://api.openweathermap.org/data/2.5/weather?"
            "lat=%s&lon=%s&units=Imperial&APPID=45711237fdbd1760b875dc764f00e097" % (lat,lon))
        #fire a quest to the url and turn the response into a string
        string = urllib2.urlopen(url).read()
        #turning string into python dictionary
        dictionary = json.loads(string)
        #getting main data out of dictionary
        main_data = dictionary["main"]
        #getting temperature out of main data dictionary
        #set up template vars
        if lat == "" or lon == "":
            form = True
            how_hot = "Waiting for temperature data"
        else:
            form = False
            how_hot = main_data["temp"]
            temp = Temperature(temperature=float(how_hot), latitude=float(lat),
                longitude=float(lon), created=datetime.datetime.now())
            temp.put()

        template_vars = {"temperature": how_hot, "form": form}
        #rendering template with template vars
        self.response.write(template.render(template_vars))



class Post(ndb.Model):
    username= ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    likes = ndb.IntegerProperty()
    dislikes = ndb.IntegerProperty()
    comments = ndb.Structure(repeated=True)

class Comment(ndb.Model):
    username = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()



class BlogHandler(webapp2.RequestHandler):
    def post(self):
        # update the blog
        post = Post(username="rob", text="first", likes=0, dislikes=400,
            comments=[])
        post.put()

    def get(self):
        # display all the posts
        # update the blog
        post = Post(username="rob", text="first", likes=0, dislikes=400,
            comments=[])
        post.put()
        posts = Post.query().fetch()
        template = jinja_environment.get_template("templates/posts.html")
        template_vars = {"posts": posts}
        self.response.write(template.render(template_vars))
        #a box for new posts if you are signed in user




jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/temperature', TemperatureHandler),
    ('/blog', BlogHandler)
], debug=True)
