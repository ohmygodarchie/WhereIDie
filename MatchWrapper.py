#returns a location object, (0,0) mean bomb was not planted
#returns None if round number was not found
#roundnumber is indexed from 0
class Match_Wrapper:
    match = None
    def __init__(self,match):
        self.match = match
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