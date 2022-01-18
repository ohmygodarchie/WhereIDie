import json
import requests
import sys
from ratelimit import limits, sleep_and_retry
from . import Constants

#make a request to the API
class apihandler:
    apikey=Constants.API_KEY
    def __init__(self) -> None:
        self.get_content()
    
    TWO_MINUTE = 60*2 + 10
    @sleep_and_retry
    @limits(calls=20, period=1)
    @sleep_and_retry
    @limits(calls=100, period=TWO_MINUTE)
    def response(self,url):
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: API request unsuccessful. {}".format(response.status_code))
            sys.exit(1)
        return response.json()
    def urlset(self,reqtype):
        url = 'https://americas.api.riotgames.com'
        url += reqtype
        url += '?api_key=' + self.apikey #api key can be set in request header need more research
        return url

    def getvalpuuid(self,gamename,tagline):
        url = self.urlset('/riot/account/v1/accounts/by-riot-id/'+gamename+'/'+tagline)
        return self.response(url)

    def getvalname_tag(self,puuid):
        url = self.urlset('/riot/account/v1/accounts/by-puuid/'+str(puuid))
        return self.response(url)

    def getmatchlist(self,puuid):
        url = self.urlset('/val/match/v1/matchlists/by-puuid/'+str(puuid))
        return self.response(url)

    def getvalmatch(self,matchid):
        url = self.urlset('/val/match/v1/matches/'+str(matchid))
        return self.response(url)
    def get_recent_games_by_queue(self,queueId):
        url = self.urlset('/val/match/v1/recent-matches/by-queue/'+str(queueId))
        return self.response(url)
    def get_content(self):
        url = 'https://na.api.riotgames.com/val/content/v1/contents?locale=en-US&api_key=' + self.apikey
        response = self.response(url)
        for x in response['maps']:
            try:
                Constants.MAPS[x['assetPath']] = x['name']
            except KeyError:
                continue
        for x in response['characters']:
            Constants.AGENTS[x['id']] = x['name']
        
        for x in response['equips']:
            Constants.WEAPONS[x['id']] = x['name']