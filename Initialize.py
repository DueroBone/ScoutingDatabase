import datetime
import os
import sys
from BasicFunctions import Log
import ImportantVariables as IV
import Config
import importlib
import re
import requests


def importMod(package):
    try:
        importlib.import_module(package)
        Log(f"Package {package} already installed")
    except (ImportError, ModuleNotFoundError):
        Log(f"{package} not installed", 1)
        import subprocess
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])
        globals()[package] = importlib.import_module(package)
        Log(f"Installed {package}")


def gatherRequirements():
    importMod("cherrypy")
    importMod("statbotics")
    import statbotics
    IV.apiStatbotics = statbotics.Statbotics()



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
    possCurrentEvents = [match for match in currentEvents if IV.eventName.lower() in match.lower()]
    if len(possCurrentEvents) == 1:
        IV.trueEventName = possCurrentEvents[0]
    else:
        IV.trueEventName = possCurrentEvents[int(input(f"Input index of actual event name: {possCurrentEvents}"))]
    Log(f"Actual  event name: {IV.trueEventName}")
    print(f"Actual  event name: {IV.trueEventName}")

    possCurrentEvents = []
    currentEvents = IV.apiStatbotics.get_events(district=Config.District, year=datetime.datetime.today().year)
    for event in currentEvents:
        if event.get('name') == IV.trueEventName:
            IV.trueEventKey = event.get('key')



def initialize():
    Log("Starting server")

    Log("Gathering depedencies")
    gatherRequirements()

    if not os.path.isdir(f"{Config.DataFolderName}"):
        os.mkdir(f"{Config.DataFolderName}")
        Log(f"Making {Config.DataFolderName} directory", 2)
    Folders = os.walk(f"{Config.DataFolderName}").__next__()[1]
    inputName = input(
        f"What is the event?  Enter new name, or index of saved events:\n{Folders}\n")
    if inputName.isdigit():
        IV.eventName = Folders[int(inputName)]
    else:
        IV.eventName = inputName
    Log(f"Selected event: {IV.eventName}")

    if not os.path.isdir(f"{Config.DataFolderName}/{IV.eventName}"):
        Log(f"Making event directory: {IV.eventName}", 1)
        os.mkdir(f"{Config.DataFolderName}/{IV.eventName}")
    IV.dataPath = f"{Config.DataFolderName}/{IV.eventName}"

    if IV.trueEventName == "":
        getOngoingEvent()

    Log("Getting teams from TBA")
    IV.teams = getTeamsInEvent()
    Log(f"{len(IV.teams)} teams in event: {IV.teams}")

    Log("Setting up teams")
    setupTeams(IV.teams, IV.dataPath)
    Log("Teams set up")

    if not os.path.isdir(f"{IV.dataPath}/{Config.IncomingFolderName}"):
        os.mkdir(f"{IV.dataPath}/{Config.IncomingFolderName}")
        Log("Making incoming data directory")

    Log("Direct online satilites to here", 3)
    IV.isRunning = True
    Log("Server started")
