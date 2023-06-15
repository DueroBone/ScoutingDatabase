# import os, Initialize
from datetime import datetime
from threading import Thread
from time import sleep

import cherrypy
from BasicFunctions import Log
from Initialize import initialize
from Running import backend
import ImportantVariables as IV
import BasicFunctions as BF


def stopServer(thread):
    IV.isRunning = False
    Log("Shutting down server", 2, True)
    thread.join()
    Log("Shutting down web server")
    cherrypy.engine.exit()
    Log("Finished", 2, True)


def startServer():
    initialize()
    sleep(0.1)
    print(f"\nServer started at {datetime.now().ctime()}\n\n\n")

    # create thread to continually run in background to do all of the proccessing
    backendThread = Thread(target=backend)
    backendThread.start()

    print("Input 'help' to print all commands")
    command = ""
    while IV.isRunning:
        # May want to not have any console level commands available?
        command = input("Input command: ").lower()
        Log("Command inputted: " + command)
        if command == "help":
            print("\nhelp: what you see right now\nstop: stops\nrestart: restarts\n")
        elif command == "stop":
            stopServer(backendThread)
            exit()
        elif command == "restart":
            stopServer(backendThread)
            startServer()
        else:
            print("Unrecognized command! Type help for more info")
    Log("--End of script--", 1)


if __name__ == "__main__":
    startServer()