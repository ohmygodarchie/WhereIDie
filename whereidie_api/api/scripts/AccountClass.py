import json
import sys
from . import getinfo
from . import MatchClasses
from . import Constants


class Account:
    # puuid="" 
    # gamename=""
    # tagline=""
    # matchlist = None
    # listofmatches = []
    # api=None
    def __init__(self,accountDto,api_obj):
        self.puuid = accountDto["puuid"]
        self.gamename = accountDto["gameName"]
        self.tagline = accountDto["tagLine"]
        self.api = api_obj
        matchlistrepsonse = self.api.getmatchlist(self.puuid)
        self.listofmatches=[]
        self.matchlist = MatchList(matchlistrepsonse)
        self.__populate_listofmatches()
    def __populate_listofmatches(self):
        #populates actual Match objects for account
        for match in self.matchlist.matchlistentries:
            matchresponse = self.api.getvalmatch(match.matchid)
            self.listofmatches.append(MatchClasses.Match(matchresponse,match))
        
class MatchList:
    # puuid = ""
    # matchlistentries = []
    def __init__(self,matchlistdto) -> None:
        self.puuid = matchlistdto['puuid']
        self.matchlistentries=[]
        self.__setmatchlist(matchlistdto['history'])
    def __setmatchlist(self,matchlistdto):
        #populates matchlist entry objects to list
        for matchlistentry in matchlistdto:
            self.matchlistentries.append(MatchListEntry(matchlistentry))

class MatchListEntry:
    # matchId=""
    # gameStartTimeMillis =-1
    # teamId = ""
    def __init__(self,matchlistentrydto) -> None:
        self.matchId = matchlistentrydto['matchId']
        self.gameStartTimeMillis = matchlistentrydto['gameStartTimeMillis']
        self.teamId = matchlistentrydto['teamId']
##APII rate limiting test
# x = getinfo.apihandler(Constants.API_KEY)
# i=0
# while(True):
#     i+=1
#     myacc = Account(x.getvalpuuid("ohmygodarchie","001"),x)

#     print(myacc.puuid,i)