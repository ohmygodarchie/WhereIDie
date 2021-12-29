
class Locations:
    x=0
    y=0
    def __init__(self,x,y):
        self.x = x
        self.y = y

class PlayerLocations:
    puuid=""
    viewRadians=-1
    #list of locations
    locations = []
    def __init__(self,PlayerLocationsDto):
        self.puuid = PlayerLocationsDto['puuid']
        self.viewRadians= PlayerLocationsDto['viewRadians']
        self.__setlocations(PlayerLocationsDto['locations'])
    def __setlocations(self,locations):
        for x in locations:
            self.locations.append(Locations(locations[x]['x'],locations[x]['y']))
    