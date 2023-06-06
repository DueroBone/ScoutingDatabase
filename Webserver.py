import cherrypy
import ImportantVariables as IV
import Config


class mySite(object):
    cherrypy.config.update({'autoreload': False})

    @cherrypy.expose
    def index(self):
        return f"Current event: {IV.trueEventName}"

    @cherrypy.expose
    def team(self, team=0):
        if int(team) == 0:
            return str(IV.teams)
        else:
            return dict(open(f"{IV.dataPath}/Teams/{team}/{Config.ScrapedInfoFileName}").read())


if __name__ == "__main__":
    print("Start the server from StartServer.py, not here!")
    from StartServer import startServer
    startServer()
