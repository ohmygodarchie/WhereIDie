import accounthandling
import getinfo
import playerClass
import LocationHandler
class round:
    roundnum=-1
    roundResult=""
    roundCeremony=""
    winningTeam=""
    bombPlanter="" #puuid
    bombDefuser = "" #puuid
    plantRoundTime = -1
    plantPlayerLocations = [] #make this a list of Playerlocations
    def __init__(self,roundDto):
        self.roundnum = roundDto['roundNumber']
        self.roundResult = roundDto['roundResult']
        self.roundCeremony = roundDto['roundCeremony']
        self.winningTeam = roundDto['winningTeam']
        self.bombPlanter = roundDto['bombPlanter']
        self.bombDefuser = roundDto['bombDefuser']
        self.plantRoundTime = roundDto['plantRoundTime']
        self.__setplantPlayerLocations(roundDto['plantPlayerLocations'])

    def __setplantPlayerLocations(self,playerlocations):
        #assumes roundDto['plantPlayerLocations'] is a list of playerlocations
        #if not, will need to be changed
        for x in playerlocations:
            #need to create PlayerLocation object
            self.plantPlayerLocations.append(LocationHandler.PlayerLocations(playerlocations[x]))

class match:
    def __init__(self) -> None:
        pass