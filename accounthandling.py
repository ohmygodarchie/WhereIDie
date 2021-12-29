import json
import sys
import getinfo
class account:
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
        self.matchlist = self.api.getmatchlist(self.puuid)
    def get_user_matchlist(self):
        return self.matchlist

#testing just getting puuid
#matchlist cant be populated due to api key restrictions
apiobj = getinfo.apihandler('RGAPI-530908f5-16fa-4d62-a692-e13c8df520a8')
accountobj = account(apiobj,"ohmygodarchie","001")
print(accountobj.puuid)