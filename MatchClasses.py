import playerClass
import LocationHandler
import KillClass
class Round:
    roundnum=-1
    roundResult=""
    roundCeremony=""
    winningTeam=""
    bombPlanter="" #puuid
    bombDefuser = "" #puuid
    plantRoundTime = -1
    plantPlayerLocations = [] 
    playerRoundStats = [] #playerRoundStats in KillClass.py
    roundResultCode =""
    def __init__(self,roundDto):
        self.roundnum = roundDto['roundNumber']
        self.roundResult = roundDto['roundResult']
        self.roundCeremony = roundDto['roundCeremony']
        self.winningTeam = roundDto['winningTeam']
        self.bombPlanter = roundDto['bombPlanter']
        self.bombDefuser = roundDto['bombDefuser']
        self.plantRoundTime = roundDto['plantRoundTime']
        self.__setplantPlayerLocations(roundDto['plantPlayerLocations'])
        self.roundResultCode = roundDto['roundResultCode']
        self.__setplayerRoundStats(roundDto['playerRoundStats'])
    def __setplayerRoundStats(self,playerRoundStats):
        #assumes roundDto['playerRoundStats'] is a list of playerRoundStats
        #if not, will need to be changed
        # no clue how to see round stats for each round yet. does it send each player's stats per round (as in all 10 in the same order every time)?
        for x in playerRoundStats:
            #need to create PlayerRoundStats object
            self.playerRoundStats.append(KillClass.PlayerRoundStats(playerRoundStats[x]))

    def __setplantPlayerLocations(self,playerlocations):
        #assumes roundDto['plantPlayerLocations'] is a list of playerlocations
        #if not, will need to be changed
        for x in playerlocations:

            self.plantPlayerLocations.append(LocationHandler.PlayerLocations(playerlocations[x]))

class Match:
    matchinfo = None 
    players=[] # list of Players
    coaches=[] # list of coaches
    teams = [] #list of teams
    roundresults = [] #list of rounds
    def __init__(self,matchDto) -> None:
        self.matchinfo = MatchInfo(matchDto['matchInfo'])
        self.players = self.__setplayers(matchDto['players'])
        self.coaches = self.__setcoaches(matchDto['coaches'])
        self.teams = self.__setteams(matchDto['teams'])
        self.roundresults = self.__setrounds(matchDto['roundResults'])
    def __setplayers(self,players):
        #assumes players is a list of playerDto
        #if not, will need to be changed
        for x in players:
            self.players.append(playerClass.Player(players[x]))
    def __setcoaches(self,coaches):
        #assumes coaches is a list of coachDto
        #if not, will need to be changed
        for x in coaches:
            self.coaches.append(playerClass.Coach(coaches[x]))
    def __setteams(self,teams):
        #assumes teams is a list of teamDto
        #if not, will need to be changed
        for x in teams:
            self.teams.append(playerClass.Team(teams[x]))
    def __setrounds(self,rounds):
        #assumes rounds is a list of roundDto
        #if not, will need to be changed
        for x in rounds:
            self.roundresults.append(Round(rounds[x]))
    def assignPlayerstoTeams(self):
        #assumes teams and players are populated
        #assigns players to teams
        #pretty inefficient could be improved in later versions
        for x in self.teams:
            for y in self.players:
                if x.teamId == y.teamId:
                    x.setTeamPlayer(y)

class MatchInfo:
    matchId = ""
    mapId = ""
    gameLengthMillis = -1
    gameStartMillis = -1
    provisioningFlowId = ""
    IsCompleted = False
    customeGameName = ""
    queueId=""
    gameMode = ""
    isRanked = False
    seasonId = ""
    def __init__(self,matchInfoDto):
        self.matchId = matchInfoDto['matchId']
        self.mapId = matchInfoDto['mapId']
        self.gameLengthMillis = matchInfoDto['gameLengthMillis']
        self.gameStartMillis = matchInfoDto['gameStartMillis']
        self.provisioningFlowId = matchInfoDto['provisioningFlowId']
        self.IsCompleted = matchInfoDto['IsCompleted']
        self.customeGameName = matchInfoDto['customeGameName']
        self.queueId = matchInfoDto['queueId']
        self.gameMode = matchInfoDto['gameMode']
        self.isRanked = matchInfoDto['isRanked']
        self.seasonId = matchInfoDto['seasonId']
