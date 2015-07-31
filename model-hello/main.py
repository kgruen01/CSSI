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
from google.appengine.ext import ndb
import jinja2
import os
import logging
import datetime

class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    school = ndb.StringProperty(required=True)
    club = ndb.StringProperty(required=False)
    attended_cssi = ndb.BooleanProperty(required=False)
    created_date = ndb.DateTimeProperty(required=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/index.html")
        self.response.write(template.render())

class AddStudentHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/add-student.html")
        self.response.write(template.render())

class StudentCreateHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("name")
        school = self.request.get("school")
        club = self.request.get("club")
        attended_cssi = self.request.get("attended_cssi")
        current_date = datetime.datetime.now()
        if (attended_cssi == "on"):
            attended_cssi_bool = True
        else:
            attended_cssi_bool = False
        student = Student(name=name, school=school, club=club,
            attended_cssi=attended_cssi_bool)
        student.created_date = current_date
        student.put()
        self.response.write("Student was created")
        self.response.write("<a href='/add_student'>Add Student</a>")

class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        query = Student.query()
        student_data = query.fetch()
        # names = []
        # for student in student_data:
        #     names.append(student.name)
        template_vars = {"students": student_data}
        template = jinja_environment.get_template("templates/list-students.html")
        self.response.write(template.render(template_vars))


class StudentViewHandler(webapp2.RequestHandler):
    def get(self):
        student_id = self.request.get("student_id")
        student = Student.get_by_id(int(student_id))
        template_vars = {"student": student}
        template = jinja_environment.get_template("templates/view-student.html")
        self.response.write(template.render(template_vars))



jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add_student', AddStudentHandler),
    ('/student/create', StudentCreateHandler),
    ('/student/list', StudentListHandler),
    ('/student/view', StudentViewHandler)
], debug=True)
