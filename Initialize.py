import os
from BasicFunctions import Log
from ImportantVariables import *


def getTeamsInEvent():
    print("!!!Get teams from online")
    return [4485, 7192]


def initialize():
    Log("Starting server")

    Log("Gathering global variables")
    global eventName
    global teams

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
        Log(f"Making event folder {eventName}", 1)
        os.mkdir(f"{DataFolderName}/{eventName}")

    teams = getTeamsInEvent()
    Log(f"Teams in event: {teams}")
