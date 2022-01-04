import playerClass
import LocationClasses
import KillClass
import json
class Round:
    # roundnum=-1
    # roundResult=""
    # roundCeremony=""
    # winningTeam=""
    # bombPlanter="" #puuid
    # bombDefuser = "" #puuid
    # plantRoundTime = -1
    # plantPlayerLocations = [] 
    # playerRoundStats = [] #playerRoundStats in KillClass.py
    # roundResultCode =""
    # defusePlayerLocations = []
    # defuseLocation = None
    # plantLocation = None
    def __init__(self,roundDto):
        self.roundnum = roundDto['roundNum']
        self.roundResult = roundDto['roundResult']
        self.roundCeremony = roundDto['roundCeremony']
        self.winningTeam = roundDto['winningTeam']
        self.playerRoundStats=[]
        self.plantPlayerLocations=[]
        self.defusePlayerLocations=[]
        if 'bombPlanter' in roundDto:
            self.bombPlanter = roundDto['bombPlanter']

        if 'bombDefuser' in roundDto:
            self.bombDefuser = roundDto['bombDefuser']

        self.plantRoundTime = roundDto['plantRoundTime']

        self.plantLocation = LocationClasses.Locations(roundDto['plantLocation'])
        if roundDto['plantPlayerLocations'] != None:
            self.__setplantPlayerLocations(roundDto['plantPlayerLocations'])
    
        self.roundResultCode = roundDto['roundResultCode']

        if roundDto['defusePlayerLocations'] != None:
            self.__setdefusePlayerLocations(roundDto['defusePlayerLocations'])

        
        self.defuseLocation = LocationClasses.Locations(roundDto['defuseLocation'])

        self.plantRoundTime = roundDto['plantRoundTime']


        self.roundResultCode = roundDto['roundResultCode']
        self.__setplayerRoundStats(roundDto['playerStats'])

        if 'defuseLocation' in roundDto:
            self.defuseLocation = LocationClasses.Locations(roundDto['defuseLocation'])


    def __setplayerRoundStats(self,playerRoundStats):
        #assumes roundDto['playerRoundStats'] is a list of playerRoundStats
        #if not, will need to be changed
        # no clue how to see round stats for each round yet. does it send each player's stats per round (as in all 10 in the same order every time)?
        for x in playerRoundStats:
            print("setting player stats for round", self.roundnum)
            self.playerRoundStats.append(KillClass.PlayerRoundStats(x))

    def __setplantPlayerLocations(self,playerlocations):
        #assumes roundDto['plantPlayerLocations'] is a list of playerlocations
        #if not, will need to be changed
        for x in playerlocations:
            self.plantPlayerLocations.append(LocationClasses.PlayerLocations(x))
    def __setdefusePlayerLocations (self,defusePlayerLocations):
        #assumes defusePlayerLocations is a list of playerlocations
        #if not, will need to be changed
        for x in defusePlayerLocations:
            self.defusePlayerLocations.append(LocationClasses.PlayerLocations(x))

class Match:
    #players=[] # list of Players
    #coaches=[] # list of coaches
    # teams = [] #list of teams
    # roundresults = [] #list of rounds
    #associate a matchlist entry to each match so information can be pulled if needed (e.g. match id, team, start time, etc)
    def __init__(self,matchDto,matchlistentry) -> None:
        self.players =[]
        self.teams=[]
        self.roundresults=[]
        self.matchinfo = MatchInfo(matchDto['matchInfo'])
        self.players = self.__setplayers(matchDto['players'])
        self.coaches = self.__setcoaches(matchDto['coaches'])
        self.teams = self.__setteams(matchDto['teams'])
        self.roundresults = self.__setrounds(matchDto['roundResults'])
        self.matchlistentry = matchlistentry
        self.assignPlayerstoTeams()
    def __init__(self,matchDto):
        self.players =[]
        self.teams=[]
        self.roundresults=[]
        self.matchinfo = MatchInfo(matchDto['matchInfo'])
        self.__setplayers(matchDto['players'])
        self.__setteams(matchDto['teams'])
        self.__setrounds(matchDto['roundResults'])
        self.assignPlayerstoTeams()
    def __setplayers(self,players):
        #assumes players is a list of playerDto
        #if not, will need to be changed
        for x in players:
            self.players.append(playerClass.Player(x))
    def __setcoaches(self,coaches):
        #assumes coaches is a list of coachDto
        #if not, will need to be changed
        for x in coaches:
            self.coaches.append(playerClass.Coach(x))
    def __setteams(self,teams):
        #assumes teams is a list of teamDto
        #if not, will need to be changed
        for x in teams:
            self.teams.append(playerClass.Team(x))
    def __setrounds(self,rounds):
        #assumes rounds is a list of roundDto
        #if not, will need to be changed
        for x in rounds:
            self.roundresults.append(Round(x))
    def assignPlayerstoTeams(self):
        #assumes teams and players are populated
        #assigns players to teams
        #pretty inefficient could be improved in later versions
        for x in self.teams:
            for y in self.players:
                if x.teamId.upper()== y.team:
                    x.setTeamPlayer(y)
    def assignCoachesToTeams(self):
        #assumes teams and coaches are populated
        #assigns coaches to teams
        #pretty inefficient could be improved in later versions
        for x in self.teams:
            for y in self.coaches:
                if x.teamId.upper() == y.teamId:
                    x.setTeamCoach(y)

class MatchInfo:
    def __init__(self,matchInfoDto):
        self.matchId = matchInfoDto['matchId']
        self.mapId = matchInfoDto['mapId']
        self.gameLengthMillis = matchInfoDto['gameLengthMillis']
        self.gameStartMillis = matchInfoDto['gameStartMillis']
        self.provisioningFlowId = matchInfoDto['provisioningFlowId']
        self.IsCompleted = matchInfoDto['isCompleted']
        self.customGameName = matchInfoDto['customGameName']
        self.queueId = matchInfoDto['queueId']
        self.gameMode = matchInfoDto['gameMode']
        self.isRanked = matchInfoDto['isRanked']
        self.seasonId = matchInfoDto['seasonId']


#test match
f = open("Match.json")
match = Match(json.load(f))
for x in match.players:
    print(x.puuid , x.team)
for y in match.roundresults[1].playerRoundStats:
    print(y.puuid)