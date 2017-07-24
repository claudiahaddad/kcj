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
        self.reponse.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', EntryPage),
    ("/home", HomePage)
], debug=True)
