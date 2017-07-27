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

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    template = jinja_environment.get_template('Login.html')
    # If the user is logged in...
    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
      if cssi_user:
        self.response.write('''
            Welcome %s %s (%s)! <br> %s <br>''' % (
              cssi_user.first_name,
              cssi_user.last_name,
              email_address,
              signout_link_html))
      # If the user hasn't been to our site, we ask them to sign up
      else:
        self.response.write(template.render())
    # Otherwise, the user isn't logged in!
    else:
      self.response.write('''
        Please log in to use our site! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/')))

  def post(self):
    user = users.get_current_user()
    if not user:
      # You shouldn't be able to get here without being logged in
      self.error(500)
      return
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    cssi_user.put()
    self.response.write('Thanks for signing up, %s! Your email haas been stored as, %s.' % email_address )

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
            water =(((weight/2.2) * 40)/ 28.3)
        elif age < 55 and age >= 30:
            water = weight / 2.2 * 35 / 28.3
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
