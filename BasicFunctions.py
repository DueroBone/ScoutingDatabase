import os
import datetime
import ImportantVariables as IV
import json
logFile = ""
logName = datetime.datetime.now().ctime()


def makeLogFile():
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    global logFile
    logFile = open(f"Logs/{logName}.txt", "a", 1)
    Log("Creating logfile")


def Log(Input, level=0, Print=False):
    """Input is what will be written down. Level is severity. Print is whether or not to print to cli as well.\n
    0 = standard\n
    1 = !\n
    2 = #\n
    3 = TODO"""
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
    if Print:
        print(Input)
    return logFile


def roundDataIn(Team, RoundNum, Scouter="", Cones=0, Cubes=0, Endgame=0):
    # Put comments below:
    """Person is the person inputting the data"""
    newDataDict = dict({'team': str(Team), 'round': int(
        RoundNum), 'scouter': Scouter, 'cones': Cones, 'cubes': Cubes, 'endgame': Endgame})

    dataFilePath = f"{IV.dataPath}/Teams/{Team}/round{RoundNum}"
    if not os.path.exists(dataFilePath):
        dataFile = open(dataFilePath, "x+")
        dataFile.write(json.dumps(newDataDict))
        dataFile.close()
        return "Created round file"
    else:
        dataFileOrig = dict(json.loads(open(dataFilePath, "rt").read()))
        changedItems = []
        changedItemsValue = []
        for newKey in newDataDict.keys():
            if newDataDict[newKey] != dataFileOrig[newKey] and newDataDict[newKey] != "" and newDataDict[newKey] != 0:
                changedItems.append(newKey)
                changedItemsValue.append(newDataDict[newKey])
        for i in range(len(changedItems)):
            # find new value
            dataFileOrig[changedItems[i]] = str(changedItemsValue[i])
        dataFile = open(dataFilePath, "w")
        dataFile.write(json.dumps(dataFileOrig))
        dataFile.close()
        return "Updated"

def roundDataOut(Team, RoundNum):
    return dict(json.loads(open(f"{IV.dataPath}/Teams/{Team}/round{RoundNum}", "r").read()))