# import os, Initialize
from threading import Thread
from BasicFunctions import Log
from Initialize import initialize
from Running import backend
import ImportantVariables as IV


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
    while IV.isRunning:
        # May want to not have any console level commands available?
        command = input("Input command: ").lower()
        if command == "help":
            print("\nhelp: what you see right now\nstop: stops the server TODO\n")
        if command == "stop":
            IV.isRunning = False
            Log("Shutting down server",2)

    Log("--End of script--", 1)


startServer()
