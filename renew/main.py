import jinja2
import logging
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import time
import datetime
from datetime import timedelta


jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class EntryPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('EntryPage/entry.html')
        self.response.out.write(template.render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("Home/home.html")
        relationship_template = jinja_environment.get_template("Relationship/Relationship.html")
        finance_template = jinja_environment.get_template("Finance/Finance.html")
        health_template = jinja_environment.get_template("Health/Health.html")
        career_template = jinja_environment.get_template("Career/Career.html")
        school_template = jinja_environment.get_template("School/School.html")
        concern_value = self.request.get('Concern')
        logging.info('HomePage handler got concern_value: ' + concern_value)
        name_value = self.request.get("Name")
        if concern_value == "Relationships":
            self.response.write(relationship_template.render({
            'Name' : name_value,
            'Concern' : self.request.get('Concern')}))
        elif concern_value == "Finance":
            self.response.write(finance_template.render({
            'Name' : name_value,
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        elif concern_value == "Health":
            self.response.write(health_template.render({
            'Name' : name_value,
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        elif concern_value == "Career":
            self.response.write(career_template.render({
            'Name' : name_value,
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        elif concern_value == "School":
            self.response.write(school_template.render({
            'Name' : name_value,
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        else:
            self.response.write(template.render({
            'Name' : name_value ,
            'Concern' : self.request.get('Concern')}))


class SleepApp(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("Sleep/sleepapp.html")
        self.response.write(template.render({
        'Name' : self.request.get('Name'),
        'time': self.request.get('time'),
        }))

class Bedtime(webapp2.RequestHandler):
    def get(self):
        time = self.request.get('time')
        time = datetime.datetime.strptime(time, '%H:%M %p')
        time2 = time.strftime('%I:%M')
        hour, minute = time2.split(":")
        hour = int(hour)
        rem = 12
        rem2 = 10
        rem3 = 8
        rem4 = 6
        rem5 = 4
        rem6 = 2
        new_hour6 = hour - rem
        new_hour5 = hour - rem2
        new_hour = hour - rem3
        new_hour2 = hour - rem4
        new_hour3 = hour - rem5
        new_hour4 = hour - rem6
        if new_hour6 <= 0:
            new_hour6 = str(12 + new_hour6)
        else:
            new_hour6 = str(new_hour6)
        if new_hour5 <= 0:
            new_hour5 = str(12 + new_hour5)
        else:
            new_hour5 = str(new_hour5)
        if new_hour <= 0:
            new_hour = str(12 + new_hour)
        else:
            new_hour = str(new_hour)
        if new_hour2 <= 0:
            new_hour2 = str(12 + new_hour2)
        else:
            new_hour2 = str(new_hour2)
        if new_hour3 <= 0:
            new_hour3 = str(12 + new_hour3)
        else:
            new_hour3 = str(new_hour3)
        if new_hour4 <= 0:
            new_hour4 = str(12 + new_hour4)
        else:
            new_hour4 = str(new_hour4)
        new_time = ":".join([new_hour, minute])
        new_time2 = ":".join([new_hour2, minute])
        new_time3 = ":".join([new_hour3, minute])
        new_time4 = ":".join([new_hour4, minute])
        new_time5 = ":".join([new_hour5, minute])
        new_time6 = ":".join([new_hour6, minute])
        template = jinja_environment.get_template("Sleep/bedtime.html")
        self.response.write(template.render({
        'Name' : self.request.get('Name'),
        'time': self.request.get('time'),
        'new_time' : new_time,
        'new_time2' : new_time2,
        'new_time3' : new_time3,
        'new_time4' : new_time4,
        'new_time5' : new_time5,
        'new_time6' : new_time6
        }))


class Person(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.StringProperty()
    weight = ndb.StringProperty()
    height = ndb.StringProperty()
    gender = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        query = Person.query()
        query = query.order(Person.name)
        people = query.fetch()
        template = jinja_environment.get_template('facts.html')
        self.response.write(template.render({"name" : Person}))

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Water/water.html')
        self.response.write(template.render())

class ResultHandler(webapp2.RequestHandler):
    def get(self):

        age = self.request.get("age")
        age = int(age)
        weight = self.request.get("weight")
        weight = int(weight)

        if age < 30:
            water =(((weight/2) * 40)/ 28.3)
        elif age < 55 and age >= 30:
            water =(((weight/2) * 35 / 28.3)
        elif age > 55:
            water = (((weight/2) * 30 / 28.3)
        else:
            water = ("???")

        template = jinja_environment.get_template('facts.html')
        self.response.write(template.render({
            "name" : self.request.get("name"),
            "water" : "{:.0f}".format(water)
            }))

class Music(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Music/music.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', EntryPage),
    ("/home", HomePage),
    ("/sleepapp", SleepApp),
    ("/bedtime", Bedtime),
    ('/mh', MainHandler),
    ("/water", NewEventHandler),
    ("/results", ResultHandler),
    ('/music', Music)
], debug=True)
