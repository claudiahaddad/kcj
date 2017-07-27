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
        time2 = time.strftime('%I:%M %p')
        hour, minute = time2.split(":")
        minute, ori_midday = minute.split(" ")
        logging.info('Midday value is equivalent to: ' + ori_midday)
        hour = int(hour)
        if ori_midday == "AM" and hour < 12:
            midday = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday = "PM"
        else:
            midday = "AM"
        logging.info('Midday1 value is equivalent to: ' + midday)
        if ori_midday == "AM" and hour < 10:
            midday1 = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday1 = "PM"
        else:
            midday1 = "AM"
        logging.info('Midday2 value is equivalent to: ' + midday1)
        if ori_midday == "AM" and hour < 8:
            midday2 = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday2 = "PM"
        else:
            midday2 = "AM"
        logging.info('Midday3 value is equivalent to: ' + midday2)
        if ori_midday == "AM" and hour < 6:
            midday3 = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday3 = "PM"
        else:
            midday3 = "AM"
        logging.info('Midday4 value is equivalent to: ' + midday3)
        if ori_midday == "AM" and hour < 4:
            midday4 = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday4 = "PM"
        else:
            midday4 = "AM"
        logging.info('Midday5 value is equivalent to: ' + midday4)
        if ori_midday == "AM" and hour < 2:
            midday5 = "PM"
        elif ori_midday == "AM" and hour == 12:
            midday5 = "PM"
        else:
            midday5 = "AM"
        logging.info('Midday6 value is equivalent to: ' + midday5)
        new_hour6 = hour - 12
        new_hour5 = hour - 10
        new_hour = hour - 8
        new_hour2 = hour - 6
        new_hour3 = hour - 4
        new_hour4 = hour - 2
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
        new_time02 = " ".join([new_time, midday])
        new_time22 = " ".join([new_time2, midday3])
        new_time32 = " ".join([new_time3, midday4])
        new_time42 = " ".join([new_time4, midday5])
        new_time52 = " ".join([new_time5, midday1])
        new_time62 = " ".join([new_time6, midday])
        template = jinja_environment.get_template("Sleep/bedtime.html")
        self.response.write(template.render({
        'Name' : self.request.get('Name'),
        'time': self.request.get('time'),
        'new_time02' : new_time02,
        'new_time22' : new_time22,
        'new_time32' : new_time32,
        'new_time42' : new_time42,
        'new_time52' : new_time52,
        'new_time62' : new_time62
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
            water =(((weight/2.2) * 40)/ 28.3)
        elif age < 55 and age >= 30:
            water = weight /2.2 * 35 / 28.3
        elif age > 55:
            water = weight / 2.2 * 30 / 28.3
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
