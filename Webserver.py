import cherrypy
import ImportantVariables as IV

class mySite(object):
    cherrypy.config.update({'autoreload': False})
    @cherrypy.expose
    def index(self):
        return f"Current event: {IV.trueEventName}"

    @cherrypy.expose
    def team(self):
        # print("Hello world")
        return str(IV.teams)