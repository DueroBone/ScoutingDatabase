# import os, Initialize
from BasicFunctions import Log
from Initialize import initialize


def startServer():
    eventName = ""
    initialize()

    # create thread to continually run in background to do all of the proccessing
    # wait for terminal input and repeat

    Log("--End of script--", 2)
    print("\nThis is the end of the script. You done messed up...")


startServer()
