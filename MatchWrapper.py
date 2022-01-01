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
    