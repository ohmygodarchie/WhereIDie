
class Locations:
    def __init__(self,locationDto):
        #print(type(locationDto))
        self.x = locationDto['x']
        self.y = locationDto['y']

class PlayerLocations:
    # puuid=""
    # viewRadians=-1
    #list of locations
    # location = None
    def __init__(self,PlayerLocationsDto):
        self.puuid = PlayerLocationsDto['puuid']
        self.viewRadians= PlayerLocationsDto['viewRadians']
        self.location = Locations(PlayerLocationsDto['location'])
    