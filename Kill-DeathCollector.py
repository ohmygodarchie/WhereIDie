import MatchWrapper
import MatchClasses
import json
import Constants
import getinfo

## Kill death collector is going to be a script that will scan the recent games and strictly collect the kills and locations of the kills
## will probably need to filter out the matches that are not ranked and matches that are not close (13-0 , 13-6 will not be collected as they are not representative)
## will need to collect ranks to see differences between rank play style
## right now am not collecting agents but in future agents will need to be collected


#step 1: get the recent games
#step 2: get the match details map, gamemode, and rank
#step 3: get round economy
#step 4: get locations of kills in round
#step 5: store locations of victims in round along with if they were attacking or defending (marker for post plant or before plant)



def main():
    #step 1
    api_handler = getinfo.apihandler(Constants.API_KEY)
    recentmatch_list = api_handler.get_recent_games_by_queue("COMPETITIVE") #list of matchids
    for x in recentmatch_list:
        matchresponse = api_handler.getvalmatch(x.matchId)
        match = MatchClasses.Match(matchresponse)
        matchwrapper = MatchWrapper.MatchWrapper(match)
        #step 2
        mapId = match.matchinfo.mapId
        gameMode = match.matchinfo.gameMode
        rank = matchwrapper.get_avg_rank()
        #step 3

        if matchwrapper.get_round_count() >13 and matchwrapper.get_round_count() <19:
            continue
        else:
            kills =[]
            for team in match.teams:
                if team.teamId == "red":
                    red_team_players = team.players
                else:
                    blue_team_players = team.players
            for i in range(matchwrapper.get_round_count()):
                temp_round = matchwrapper.get_round(i)
                kills.append(matchwrapper.get_all_kills_in_round(i))
                
                


if __name__ == "__main__":
    main()