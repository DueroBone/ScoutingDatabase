from threading import Thread
import time
import json

from BasicFunctions import Log
import Config
import ImportantVariables as IV


def updateBackend():
    Log("Move files", 3)
    # Input


def pollApis():
    # Log("Polling Apis")
    for team in IV.teams:
        file = open(
            f"{IV.dataPath}/Teams/{team}/{Config.ScrapedInfoFileName}", "w")
        file.write(json.dumps(IV.apiStatbotics.get_team_event(team, IV.trueEventKey)))
        file.close()


def backend():
    while IV.isRunning:
        Thread(target=pollApis).start()
        for i in range(Config.ApiDelayReps):
            # Thread(target=updateBackend).start()
            time.sleep(Config.BackendDelaySec)
            if not IV.isRunning:
                break


if __name__ == "__main__":
    print("Start the server from StartServer.py, not here!")
    from StartServer import startServer
    startServer()
