# Modifying these variables could result in instability
DataFolderName = "Events"
ScrapedInfoFileName = "liveScrapedInfo"
ScoutedTeamInfoFileName = "staticScoutedInfo"
IncomingFolderName = "Input"
District = "FIN"
# -------------------------- #

# Rounds to wait before piping data into database
RoundInputDelay = 2

# Delay between updating the backend (seconds)
# 5
BackendDelaySec = 5

# How often to poll the apis (once every X backend updates)
# 6
ApiDelayReps = 2
