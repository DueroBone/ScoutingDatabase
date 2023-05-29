import statbotics
import time

from BasicFunctions import Log
from Config import *
from ImportantVariables import *


def updateBackend():
    Log("Move files", 3)
    # Input


def pollApis():
    Log("Poll TBA", 3)
    Log("Poll Statbotics", 3)
    # statbotics.get_locations("United States", "Indiana")
    # statbotics.team_event_metrics(4485, "IDk what event")


def backend():
    global BackendDelaySec
    global ApiDelayReps

    while True:
        pollApis()
        for i in range(ApiDelayReps):
            updateBackend()
            time.sleep(BackendDelaySec)
