To start the server, run StartServer.py
It will ask for an event name, check against online events, and then start the server. 
All team info are in Events/"Event name"/Teams
For team info, there is: 
    liveScrapedInfo which contains data from statbotics
    staticScoutedInfo which is information that is scouted at before the game begins
    Round"X" which details that team's observed contributions during that match.
Scouted information goes into the folder Events/"Event name"/Input, and will be filtered down to the teams folder