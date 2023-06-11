import cherrypy
import ImportantVariables as IV
import BasicFunctions as BF
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

    @cherrypy.expose
    def roundIn(self, team=-1,round=-1, person="", cones=-1, cubes=-1, endgame=-1):
        if team == -1:
            return "Add team to url input"
        if round == -1:
            return "Add round number to url input"
        if cones == -1:
            return "Add cones to url input"
        if cubes == -1:
            return "Add cubes to url input"
        if endgame == -1:
            return "Add endgame to url input"
        if person == "":
            return "Add person to url input"
        return BF.roundDataIn(team, round, person, cones, cubes, endgame)

    @cherrypy.expose
    def roundOut(self, team=-1, round=-1):
        if team == -1:
            return "Add team to input"
        if round == -1:
            return "Add round number to url input"
        return str(BF.roundDataOut(team, round))



if __name__ == "__main__":
    print("Start the server from StartServer.py, not here!")
    from StartServer import startServer
    startServer()
