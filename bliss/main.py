import jinja2
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
        if self.request.get('Concern') is 'Relationship':
            self.response.write(relationship_template.render())
        else:
            self.response.write(template.render({
            'Name' : self.request.get('Name'),
            'Concern' : self.request.get('Concern')}))

app = webapp2.WSGIApplication([
    ('/', EntryPage),
    ("/home", HomePage)
], debug=True)
