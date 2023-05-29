import os
from BasicFunctions import Log
from ImportantVariables import *
from Config import *


def getTeamsInEvent():
    Log("Not set up yet, returning hardcoded value", 3)
    return [4485, 7192]


def setupTeams(teamInput, path):
    if not os.path.isdir(f"{path}/Teams"):
        os.makedirs(f"{path}/Teams")
        Log("Making directory Teams")
    global TBATeamInfoFileName
    global ScoutedTeamInfoFileName
    for team in teamInput:
        newPath = f"{path}/Teams/{team}"

        if not os.path.isdir(newPath):
            os.makedirs(newPath)
            open(f"{newPath}/{TBATeamInfoFileName}", "x")
            open(f"{newPath}/{ScoutedTeamInfoFileName}", "x")
            Log(f"Team {team}: added")


def initialize():
    Log("Starting server")

    Log("Gathering global variables")
    global eventName
    global teams
    global dataPath
    global IncomingFolderName

    if not os.path.isdir(f"{DataFolderName}"):
        os.mkdir(f"{DataFolderName}")
        Log(f"Making {DataFolderName} directory", 2)
    Folders = os.walk(f"{DataFolderName}").__next__()[1]
    inputName = input(
        f"What is the event?  Enter new name, or index of saved events:\n{Folders}\n")
    if inputName.isdigit():
        eventName = Folders[int(inputName)]
        print(f"Resuming event {eventName}")
    else:
        eventName = inputName
    Log(f"Selected event: {eventName}")

    if not os.path.isdir(f"{DataFolderName}/{eventName}"):
        Log(f"Making event directory: {eventName}", 1)
        os.mkdir(f"{DataFolderName}/{eventName}")
    dataPath = f"{DataFolderName}/{eventName}"

    Log("Getting teams from TBA")
    teams = getTeamsInEvent()
    Log(f"{len(teams)} teams in event: {teams}")

    Log("Setting up teams")
    setupTeams(teams, dataPath)
    Log("Teams set up")

    if not os.path.isdir(f"{dataPath}/{IncomingFolderName}"):
        os.mkdir(f"{dataPath}/{IncomingFolderName}")
        Log("Making incoming data directory")

    Log("Direct online satilites to here", 3)
