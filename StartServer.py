# import os, Initialize
from threading import Thread
from BasicFunctions import Log
from Initialize import initialize
from Initialize import gatherRequirements
from Running import backend


def startServer():
    eventName = ""
    initialize()
    print("\nServer started\n\n\n")

    # create thread to continually run in background to do all of the proccessing
    backendThread = Thread(target=backend)
    backendThread.start()
    # backend()
    # wait for terminal input and repeat
    print("Input 'help' to print all commands")
    command = ""
    while True:
        # May want to not have any console level commands available?
        command = input("Input commands: ")
        if command.lower() == "help":
            print("\nhelp: what you see right now\nstop: stops the server TODO\n")

    Log("--End of script--", 2)
    print("\nThis is the end of the script. You done messed up...")


startServer()
