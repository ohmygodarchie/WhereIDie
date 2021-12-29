import json
import requests
import sys
#make a request to the API
class apihandler:
    def __init__(self,apikey) -> None:
        self.apikey = apikey 

    def response(self,url):
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: API request unsuccessful.")
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
