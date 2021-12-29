import json
import sys
import getinfo
class aAcount:
    puuid="" 
    matchlist=[]
    gamename=""
    tagline=""
    api=None
    def __init__(self,apihandler_obj,gamename,tagline):
        self.api = apihandler_obj
        self.gamename = gamename
        self.tagline = tagline
        puuidresponse = self.api.getvalpuuid(self.gamename,self.tagline)
        self.__setpuuid(puuidresponse['puuid'])
        ##blow requires higher auth api key
        #self.api.__set_user_matchlist()
    def __setpuuid(self,puuid):
        self.puuid = puuid
    def getpuuid(self):
        return self.puuid
    def __set_user_matchlist(self):
        self.matchlist = self.api.getmatchlist(self.puuid) #this will need json parsing cant test so rip
    def get_user_matchlist(self):
        return self.matchlist

#testing just getting puuid
#matchlist cant be populated due to api key restrictions
apiobj = getinfo.apihandler('RGAPI-dc863e8b-237b-4a8e-b8a3-525bfc57fd1d')
accountobj = aAcount(apiobj,"ohmygodarchie","002")
print(accountobj.puuid)