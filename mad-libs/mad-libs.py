import webapp2
import jinja2
import os
import logging
from google.appengine.api import users



class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/byebye')))
            entry = jinja_environment.get_template("templates/mad_libs_entry.html")
            self.response.write(entry.render(self.request.POST))

        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)
        logging.info("MainHandler")



class ByeByeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>ByeBye</body></html>')


class ResponseHandler(webapp2.RequestHandler):
    def post(self):
        name1 = self.request.get("name1")
        name2 = self.request.get("name2")
        name3 = self.request.get("name3")
        socialmedia = self.request.get("socialmedia")
        instrument1 = self.request.get("instrument1")
        instrument2 = self.request.get("instrument2")
        instrument3 = self.request.get("instrument3")
        number = self.request.get("number")
        holiday = self.request.get("holiday")
        adjective1 = self.request.get("adjective1")
        pluralnoun1 = self.request.get("pluralnoun1")
        songname1 = self.request.get("songname1")
        artist1 = self.request.get("artist1")
        songname2 = self.request.get("songname2")
        artist2 = self.request.get("artist2")
        dict_words = {"name1": name1, "name2": name2,
        "name3": name3, "socialmedia": socialmedia, "instrument1": instrument1,
        "instrument2": instrument2, "instrument3": instrument3, "number": number,
        "holiday": holiday, "adjective1": adjective1, "pluralnoun1": pluralnoun1,
        "songname1": songname1, "artist1": artist1, "songname2": songname2,
        "artist2": artist2}
        response = jinja_environment.get_template("templates/mad_libs_response.html")
        self.response.write(response.render())





jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/response', ResponseHandler),
    ('/byebye', ByeByeHandler)
], debug=True)
