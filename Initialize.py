import datetime
import os
from threading import Thread

import cherrypy
from BasicFunctions import Log
import ImportantVariables as IV
import Config
import re
import Webserver
import statbotics


def getTeamsInEvent():
    Log("Not set up yet, returning hardcoded value", 3)
    return [4485, 1741]


def setupTeams(teamInput, path):
    if not os.path.isdir(f"{path}/Teams"):
        os.makedirs(f"{path}/Teams")
        Log("Making directory Teams")
    for team in teamInput:
        newPath = f"{path}/Teams/{team}"

        if not os.path.isdir(newPath):
            os.makedirs(newPath)
            open(f"{newPath}/{Config.ScrapedInfoFileName}", "x")
            open(f"{newPath}/{Config.ScoutedTeamInfoFileName}", "x")
            Log(f"Team {team}: added")


def getOngoingEvent():
    currentEvents = IV.apiStatbotics.get_events(
        district=Config.District, year=datetime.datetime.today().year, fields=["name"])
    currentEvents = re.findall(r"'(.+?)'", f"{currentEvents}")[1::2]
    possCurrentEvents = [
        match for match in currentEvents if IV.eventName.lower() in match.lower()]
    if len(possCurrentEvents) == 1:
        IV.trueEventName = possCurrentEvents[0]
    else:
        IV.trueEventName = possCurrentEvents[int(
            input(f"Input index of actual event name: {possCurrentEvents}"))]
    Log(f"Actual  event name: {IV.trueEventName}", Print=True)

    possCurrentEvents = []
    currentEvents = IV.apiStatbotics.get_events(
        district=Config.District, year=datetime.datetime.today().year)
    for event in currentEvents:
        if event.get('name') == IV.trueEventName:
            IV.trueEventKey = event.get('key')
            break
    Log("Hard save the event info", 3)


def makeNewEvent():
    Log("Making new event", 1)

    Log(f"Making event directory: {IV.eventName}", 1)
    os.mkdir(f"{Config.DataFolderName}/{IV.eventName}")
    IV.dataPath = f"{Config.DataFolderName}/{IV.eventName}"

    getOngoingEvent()

    Log("Getting teams from TBA")
    IV.teams = getTeamsInEvent()
    Log(f"{len(IV.teams)} teams in event: {IV.teams}")

    Log("Setting up teams")
    setupTeams(IV.teams, IV.dataPath)
    Log("Teams set up")


def resumeEvent():
    Log("SET UP RETURNING EVENT", 3, True)
    IV.dataPath = f"{Config.DataFolderName}/{IV.eventName}"
    getOngoingEvent()

    Log("Getting teams from TBA")
    IV.teams = getTeamsInEvent()
    Log(f"{len(IV.teams)} teams in event: {IV.teams}")

    Log("Setting up teams")
    setupTeams(IV.teams, IV.dataPath)


def initialize(isNew=False):
    Log("Starting server")

    Log("Gathering depedencies")
    IV.apiStatbotics = statbotics.Statbotics()

    if not os.path.isdir(f"{Config.DataFolderName}"):
        os.mkdir(f"{Config.DataFolderName}")
        Log(f"Making {Config.DataFolderName} directory", 2)
    Folders = os.walk(f"{Config.DataFolderName}").__next__()[1]

    inputName = input(
        f"What is the event?  Enter new name, or index of saved events:\n{Folders}\n")
    if inputName.isdigit():
        IV.eventName = Folders[int(inputName)]
        resumeEvent()
    else:
        IV.eventName = inputName
        makeNewEvent()
    Log(f"Selected event: {IV.eventName}")

    Log("Starting web server")
    cherrypy.config.update(
        {'log.screen': False, 'log.access_file': '', 'log.error_file': ''})
    Thread(target=lambda: Webserver.cherrypy.quickstart(
        Webserver.mySite())).start()

    Log("Direct online satilites to here", 3)
    IV.isRunning = True

    Log("Server ready")


if __name__ == "__main__":
    print("Start the server from StartServer.py, not here!")
    from StartServer import startServer
    startServer()
