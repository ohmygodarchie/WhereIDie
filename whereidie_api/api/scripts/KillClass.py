import LocationClasses
import OtherClasses

class PlayerRoundStats:
    # puuid = ""
    # kills= [] #list of kill objects
    # damage =[] # list of damage objects
    # score=-1
    # economy=None
    # ability=None

    def __init__(self,playerRoundStatsDto):
        self.puuid = playerRoundStatsDto['puuid']
        self.score = playerRoundStatsDto['score']
        self.kills=[]
        self.damage =[]
        self.__setkills(playerRoundStatsDto['kills'])
        self.__setdamage(playerRoundStatsDto['damage'])
        self.economy = OtherClasses.Economy(playerRoundStatsDto['economy'])
        #self.ability = OtherClasses.Ability(playerRoundStatsDto['ability'])
    def __setkills(self,kills):
        for x in kills:
            self.kills.append(Kill(x))

    def __setdamage(self,damage):
        for x in damage:
            self.damage.append(Damage(x))


class Damage:
    # receiverpuuid = ""
    # damage = []
    def __init__(self,damageDto):
        self.puuid = damageDto['receiver']
        self.damage = damageDto['damage']
        self.headshots = damageDto['headshots']
        self.legshots = damageDto['legshots']
        self.bodyshots = damageDto['bodyshots']

class Kill:
    # killer ="" #puuid of killer
    # victim = "" #puuid of victim
    # victimLocation = None #LocationHandler.Locations
    # timeSinceRoundStart = -1
    # timeSinceGameStart = -1
    # assistants = [] #list of puuids
    # playerLocations = [] #list of LocationHandler.PlayerLocations
    # finishingdamage = None
    def __init__(self,killDto):
        self.killer = killDto['killer']
        self.victim = killDto['victim']
        self.victimLocation = LocationClasses.Locations(killDto['victimLocation'])
        self.timeSinceRoundStart = killDto['timeSinceRoundStartMillis']
        self.timeSinceGameStart = killDto['timeSinceGameStartMillis']
        self.assistants =[]
        self.playerLocations = []
        self.__setassistants(killDto['assistants'])
        self.__setplayerLocations(killDto['playerLocations'])
        self.finishingdamage = FinishingDamage(killDto['finishingDamage'])

    def __setassistants(self,assistants):
        for x in assistants:
            self.assistants.append(x)
    def __setplayerLocations(self,playerLocations):
        for x in playerLocations:
            self.playerLocations.append(LocationClasses.PlayerLocations(x))

class FinishingDamage:
    # damageType = ""
    # damageItem = ""
    # isSecondaryFireMode=False
    def __init__(self,finishingdamageDto):
        self.damageType = finishingdamageDto['damageType']
        self.damageItem = finishingdamageDto['damageItem']
        self.isSecondaryFireMode = finishingdamageDto['isSecondaryFireMode']
