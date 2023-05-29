import time

from BasicFunctions import Log
import Config
import ImportantVariables as IV


def updateBackend():
    Log("Move files", 3)
    # Input


def pollApis(statsModule):
    Log("Poll TBA", 3)
    Log("Poll Statbotics", 3)
    Log("Statbotics says:" +
        str(IV.m_Statbotics.get_events(district="FIN", fields=["name"])))
    # statbotics.team_event_metrics(4485, "IDk what event")


def backend():
    while True:
        pollApis(IV.m_Statbotics)
        for i in range(Config.ApiDelayReps):
            updateBackend()
            time.sleep(Config.BackendDelaySec)
