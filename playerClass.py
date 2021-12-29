
class Player:
    team =""
    agent=""
    gamename=""
    tagline=""
    puuid=""
    partyid=""
    stats =None #stats class
    rank = 0
    
    #can add player card and title can implement later
    def __init__(self, playerdto) -> None:
        self.team = playerdto['teamId']
        self.agent = playerdto['agentId']
        self.gamename = playerdto['gameName']
        self.tagline = playerdto['tagLine']
        self.puuid = playerdto['puuid']
        self.partyid = playerdto['partyId']
        self.stats = Stats(playerdto['stats'])
        self.rank = playerdto['rank']

    
class Stats:
    score =0
    roundsPlayed=0
    kills=0
    deaths=0
    assists=0
    playtime=0
    abilitycasts=None
    kda =0
    kd=0
    def __init__(self,statsdto) -> None:
        self.score = statsdto['score']
        self.roundsPlayed = statsdto['roundsPlayed']
        self.kills = statsdto['kills']
        self.deaths = statsdto['deaths']
        self.assists = statsdto['assists']
        self.playtime = statsdto['playtime']
        self.abilitycasts = AbilityCasts(statsdto['abilityCasts'])
        self.__setkda()
        self.__setkd()
    

    def __setkda(self):
        self.kda = (self.kills + self.assists)/self.deaths
    def __setkd(self):
        self.kd = self.kills/self.deaths

class AbilityCasts:
    grenadecasts=0
    ability1 = 0
    ability2 = 0
    ults = 0
    def __init__(self,abilitydto) -> None:
        self.grenadecastse = abilitydto['grenadeCasts']
        self.ability1 = abilitydto['ability1']
        self.ability2 = abilitydto['ability2']
        self.ults = abilitydto['ultimateCasts']
     
class Coach:
    puuid=0
    teamId = ""
    def __init__(self,coachdto) -> None:
        self.puuid = coachdto['puuid']
        self.teamId = coachdto['teamId']
    
class Team:
    teamname=""
    teamtag=""
    teamplayers=[]
    matchId=""
    teamcoach = None

    def __init__(self,teamdto):
        self.teamid = teamdto['teamId']
        self.teamname = teamdto['teamName']
        self.teamtag = teamdto['teamTag']

    def setTeamPlayer(self,Player):
        self.teamplayers.append(Player)

    def setTeamCoach(self,Coach):
        self.teamcoach = Coach




