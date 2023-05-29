import os
import datetime
logFile = ""
logName = datetime.datetime.now().ctime()


def makeLogFile():
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    global logFile
    logFile = open(f"Logs/{logName}.txt", "a")
    Log("Creating logfile")


def Log(Input, level=0):
    """Input is what will be written down. Level is severity. \n
    0 = standard\n
    1 = !\n
    2 = #\n
    3 = TODO\n"""
    global logFile
    if not os.path.exists(f"Logs/{logName}.txt"):
        makeLogFile()
    if level == 3:
        tags = "TODO"
    elif level == 2:
        tags = "#"
    elif level == 1:
        tags = "!"
    else:
        tags = ""
    logFile.write(
        f"{datetime.datetime.now().time().replace(microsecond=0)} >{tags}> {Input}\n")
    return logFile
