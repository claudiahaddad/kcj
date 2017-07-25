import jinja2
import logging
import os
import webapp2

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class EntryPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('entry.html')
        self.response.out.write(template.render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("home.html")
        relationship_template = jinja_environment.get_template("Relationship.html")
        finance_template = jinja_environment.get_template("Finance.html")
        health_template = jinja_environment.get_template("Health.html")
        concern_value = self.request.get('Concern')
        logging.info('HomePage handler got concern_value: ' + concern_value)
        if concern_value == "Relationships":
            self.response.write(relationship_template.render())
        elif concern_value == "Finance":
            self.response.write(finance_template.render({
            'Age' : self.request.get("Age")
            }))
        elif concern_value == "Health":
            self.response.write(health_template.render({
            'Age' : self.request.get("Age")
            }))
        else:
            self.response.write(template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern')}))


app = webapp2.WSGIApplication([
    ('/', EntryPage),
    ("/home", HomePage)
], debug=True)
