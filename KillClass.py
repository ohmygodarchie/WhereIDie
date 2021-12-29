import LocationHandler
import OtherClasses

class PlayerRoundStats:
    puuid = ""
    kills= [] #list of kill objects
    damage =[] # list of damage objects
    score=-1
    economy=None
    ability=None

    def __init__(self,playerRoundStatsDto):
        self.puuid = playerRoundStatsDto['puuid']
        self.score = playerRoundStatsDto['score']
        self.__setkills(playerRoundStatsDto['kills'])
        self.__setdamage(playerRoundStatsDto['damage'])
        self.economy = OtherClasses.Economy(playerRoundStatsDto['economy'])
        self.ability = OtherClasses.Ability(playerRoundStatsDto['ability'])
    def __setkills(self,kills):
        for x in kills:
            self.kills.append(Kill(kills[x]))

    def __setdamage(self,damage):
        for x in damage:
            self.damage.append(Damage(damage[x]))


class Damage:
    puuid = ""
    damage = []
    def __init__(self,damageDto):
        self.puuid = damageDto['puuid']
        self.damage = damageDto['damage']

class Kill:
    killer ="" #puuid of killer
    victim = "" #puuid of victim
    victimLocation = None #LocationHandler.Locations
    assistants = [] #list of puuids
    playerLocations = [] #list of LocationHandler.PlayerLocations
    finishingdamage = None
    def __init__(self,killDto):
        self.killer = killDto['killer']
        self.victim = killDto['victim']
        self.victimLocation = LocationHandler.Locations(killDto['victimLocation']['x'],killDto['victimLocation']['y'])
        self.__setassistants(killDto['assistants'])
        self.__setplayerLocations(killDto['playerLocations'])
        self.finishingdamage = FinishingDamage(killDto['finishingdamage'])

    def __setassistants(self,assistants):
        for x in assistants:
            self.assistants.append(assistants[x])
    def __setplayerLocations(self,playerLocations):
        for x in playerLocations:
            self.playerLocations.append(LocationHandler.PlayerLocations(playerLocations[x]))

class FinishingDamage:
    damageType = ""
    damageItem = ""
    isSecondaryFireMode=False
    def __init__(self,finishingdamageDto):
        self.damageType = finishingdamageDto['damageType']
        self.damageItem = finishingdamageDto['damageItem']
        self.isSecondaryFireMode = finishingdamageDto['isSecondaryFireMode']
