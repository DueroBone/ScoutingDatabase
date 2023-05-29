# import os, Initialize
from threading import Thread
from BasicFunctions import Log
from Initialize import initialize
from Running import backend


def startServer():
    eventName = ""
    initialize()

    # create thread to continually run in background to do all of the proccessing
    backendThread = Thread(target=backend)
    backendThread.start()
    # wait for terminal input and repeat
    while True:
        # May want to not have any console level commands available?
        input("Input special commands: ")

    Log("--End of script--", 2)
    print("\nThis is the end of the script. You done messed up...")


startServer()
