import os
import sys
from BasicFunctions import Log
import ImportantVariables as IV
import Config


def gatherRequirements():
    package = "statbotics"
    import importlib
    try:
        importlib.import_module(package)
    except (ImportError, ModuleNotFoundError):
        Log("Statbotics not installed", 1)
        import subprocess
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])
        globals()[package] = importlib.import_module(package)
        Log('Installed statbotics')
    import statbotics
    IV.m_Statbotics = statbotics.Statbotics()


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
            open(f"{newPath}/{Config.TBATeamInfoFileName}", "x")
            open(f"{newPath}/{Config.ScoutedTeamInfoFileName}", "x")
            Log(f"Team {team}: added")


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
        eventName = Folders[int(inputName)]
    else:
        eventName = inputName
    Log(f"Selected event: {eventName}")

    if not os.path.isdir(f"{Config.DataFolderName}/{eventName}"):
        Log(f"Making event directory: {eventName}", 1)
        os.mkdir(f"{Config.DataFolderName}/{eventName}")
    dataPath = f"{Config.DataFolderName}/{eventName}"

    Log("Getting teams from TBA")
    teams = getTeamsInEvent()
    Log(f"{len(teams)} teams in event: {teams}")

    Log("Setting up teams")
    setupTeams(teams, dataPath)
    Log("Teams set up")

    if not os.path.isdir(f"{dataPath}/{Config.IncomingFolderName}"):
        os.mkdir(f"{dataPath}/{Config.IncomingFolderName}")
        Log("Making incoming data directory")

    Log("Direct online satilites to here", 3)
    Log("Server started")
