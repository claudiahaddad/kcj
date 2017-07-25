import jinja2
import logging
import os
import webapp2
from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class EntryPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('entry.html')
        self.response.out.write(template.render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("home.html")
        relationship_template = jinja_environment.get_template("Relationship/Relationship.html")
        finance_template = jinja_environment.get_template("Finance/Finance.html")
        health_template = jinja_environment.get_template("Health/Health.html")
        concern_value = self.request.get('Concern')
        logging.info('HomePage handler got concern_value: ' + concern_value)
        if concern_value == "Relationships":
            self.response.write(relationship_template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern')}))
        elif concern_value == "Finance":
            self.response.write(finance_template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        elif concern_value == "Health":
            self.response.write(health_template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern'),
            'Age' : self.request.get("Age")
            }))
        else:
            self.response.write(template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern')}))

class SleepApp(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("sleepapp.html")
        self.response.write(template.render({
        'Name' : self.request.get('Name'),
        'Wake-Up': self.request.get('Wake-Up'),
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
        template = jinja_environment.get_template('water.html')
        self.response.write(template.render())


class ConfirmationHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('confirmation.html')
        self.response.write(template.render({
            "name" : self.request.get("name"),
            "age" : self.request.get("age"),
            "weight" : self.request.get("weight"),
            "height" : self.request.get("height"),
        }))
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


app = webapp2.WSGIApplication([
    ('/', EntryPage),
    ("/home", HomePage),
    ("/sleep", SleepApp),
    ('/mh', MainHandler),
    ("/water", NewEventHandler),
    ("/confirmation", ConfirmationHandler),
    ("/results", ResultHandler)
], debug = True)
