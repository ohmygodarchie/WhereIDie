import MatchClasses
class Match_Wrapper:
    match = None
    def __init__(self,match):
        self.match = match
    #returns a location object, (0,0) mean bomb was not planted
    #roundnumber is indexed from 0
    def get_round_plant_location(self,roundNum):
        #returns a location object
        return self.match.rounds[roundNum].plantLocation

    def get_round_defuse_location(self,roundNum):
        #returns a location object
        return self.match.rounds[roundNum].defuseLocation

    def get_round_plant_player_locations(self,roundNum):
        #returns a list of location objects
        return self.match.rounds[roundNum].defusePlayerLocations
    
    def get_round_defuse_player_locations(self,roundNum):
        #returns a list of location objects
        return self.match.rounds[roundNum].defusePlayerLocations

    def get_round_plant_time(self,roundNum):
        #returns a int in miliseconds, 0 if no bomb was planted
        return self.match.rounds[roundNum].plantTime
    
    def get_round_defuse_time(self,roundNum):
        #returns a int in miliseconds, 0 if no bomb was defused
        return self.match.rounds[roundNum].defuseTime

    def get_round_planter(self,roundNum):
        #returns a string puuid
        if self.match.rounds[roundNum].bombPlanter =="":
            return "None"
        return self.match.rounds[roundNum].bombPlanter

    def get_round_defuser(self,roundNum):
        #returns a string puuid
        if self.match.rounds[roundNum].bombDefuser =="":
            return "None"
        return self.match.rounds[roundNum].bombDefuser
    def get_round_result(self,roundNum):
        #returns a string
        return self.match.rounds[roundNum].roundResult
    def get_round_ceremony(self,roundNum):
        #returns a string
        return self.match.rounds[roundNum].roundCeremony
    def get_round_result_code(self,roundNum):
        #returns a string
        return self.match.rounds[roundNum].roundResultCode
    def get_round_winning_team(self,roundNum):
        #returns a string
        return self.match.rounds[roundNum].winningTeam
    def get_round_player_stats(self,roundNum):
        #returns a list of playerRoundStats
        return self.match.rounds[roundNum].playerRoundStats
    def get_round_num(self,roundNum):
        #returns a int
        return self.match.rounds[roundNum].roundNum
    def get_match_id(self):
        #returns a string
        return self.match.matchId
    def get_match_duration(self):
        #returns a int in miliseconds
        return self.match.matchDuration
    def get_match_start_time(self):
        #returns a int in miliseconds
        return self.match.matchStartTime
    def get_match_map(self):
        #returns a string
        return self.match.matchinfo.mapId
    def get_match_type(self):
        #returns a string of what queue it is
        return self.match.matchinfo.queueId
    def get_player_stats(self,puuid):
        #returns a stats object, if cant find player return None
        for player in self.match.players:
            if player.puuid == puuid:
                return player.stats
        return None
    def get_all_kills_in_round(self,roundNum):
        #returns a list of kills
        kills = []
        for x in self.match.rounds[roundNum].playerRoundStats:
            for y in x.kills:
                kills.append(y)
        return kills
    def get_num_of_rounds(self):
        #returns a int
        return len(self.match.roundresults)
    def get_round(self, roundNum):
        #returns a round object
        return self.match.roundresults[roundNum]

    def get_avg_rank(self):
        #returns a int
        total = 0
        for player in self.match.players:
            total += player.stats.rank
        return total/len(self.match.players)
    def get_avg_economy(self,roundNum):
        #returns a list of ints, index 0 is red team, index 1 is blue team. values are average cost of loadout for all players
        # this function can be greatly imporved to determine economic status of each team per round
        # prob add a function somewhere to determine, pistol, save, half, force, etc.
        playerroundstats = self.get_all_player_round_stats(roundNum)
        redTotal = 0
        blueTotal = 0
        for x in playerroundstats:
            if x.team == "RED":
                redTotal += x.economy.loadoutValue
            else:
                blueTotal+= x.economy.loadoutValue
        return [redTotal/5,blueTotal/5]

    def determine_economic_situation(self, playerroundstats,roundEcon, roundNum): 
        #need to determine values for save, force, and half
        if roundNum == 0 or roundNum == 12:
            return "Pistol"
        if roundEcon < 0:
            return "Save"
        if roundEcon > 0:
            return "Force"
        if roundEcon == 0:
            return "Half"