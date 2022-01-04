
class Locations:
    def __init__(self,locationDto):
        #print(type(locationDto))
        if 'x' in locationDto:
            self.x = locationDto["x"]
        if 'y' in locationDto:
            self.y = locationDto["y"]

class PlayerLocations:
    # puuid=""
    # viewRadians=-1
    #list of locations
    # location = None
    def __init__(self,PlayerLocationsDto):
        self.puuid = PlayerLocationsDto['puuid']
        self.viewRadians= PlayerLocationsDto['viewRadians']
        self.location = Locations(PlayerLocationsDto['location'])
    