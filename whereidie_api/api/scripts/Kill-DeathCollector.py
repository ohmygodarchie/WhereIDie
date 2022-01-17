from . import MatchWrapper
from . import MatchClasses
import json
from . import Constants
import csv
import os
import mysql.connector
## Kill death collector is going to be a script that will scan the recent games and strictly collect the kills and locations of the kills
## will probably need to filter out the matches that are not ranked and matches that are not close (13-0 , 13-6 will not be collected as they are not representative)
## will need to collect ranks to see differences between rank play style
## right now am not collecting agents but in future agents will need to be collected


#step 1: get the recent games
#step 2: get the match details map, gamemode, and rank
#step 3: get round economy
#step 4: get locations of kills in round
#step 5: store locations of victims in round along with if they were attacking or defending (marker for post plant or before plant)

#this is super inefficient but it works maybe????? its like 4 loops but its basically constants so maybe we can pretend its O(1)
#things in this script can probably be added to match wrapper to clean this up idk

#storage rn is csv file for testing, gonna store in a database later -- DONE STORING IN DB


## NEED TO DO, ATTAACKING / DEFENDING NEEDS TO RECOGNIZE FLIP!!!

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=Constants.MYSQL_PASSWORD,
  database="whereidie"
)

def main():
    #step 1
    # api_handler = getinfo.apihandler(Constants.API_KEY)
    # recentmatch_list = api_handler.get_recent_games_by_queue("COMPETITIVE") #list of matchids
    mycursor = mydb.cursor()

    for x in range(1):#recentmatch_list:
        #matchresponse = api_handler.getvalmatch(x.matchId)
        test = open(os.path.dirname(os.getcwd())+"/WhereIDie/testcases/match.json","r")
        
        #match = MatchClasses.Match(matchresponse)
        match = MatchClasses.Match(json.load(test))
        matchwrapper = MatchWrapper.Match_Wrapper(match)

        #step 2
        mapId = match.matchinfo.mapId
        queueId = match.matchinfo.queueId
        rank = matchwrapper.get_avg_rank()
       #filter out games here
        if matchwrapper.get_num_of_rounds() >13 and matchwrapper.get_num_of_rounds() <19: #13-5 or less not counted
            continue
        
        else:
            mapName = matchwrapper.get_map_name(mapId).upper()
            sql = "INSERT INTO kd_collector_"+mapName+" (queueid,rank_id,red_team_econ,blue_team_econ,attacker_team,victim_team,attacker_location_x,attacker_location_y,victim_location_x,victim_location_y,plant_status) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            for team in match.teams:
                if team.teamId.upper() == "Red".upper():
                    red_team_players = team.teamplayers
                else:
                    blue_team_players = team.teamplayers
            for i in range(matchwrapper.get_num_of_rounds()):
                #step 3
                #print(i)
                round_economy = matchwrapper.get_avg_economy(i) #list of ints, index 0 is red team, index 1 is blue team. values are average cost of loadout for all players
                red_team_econ = matchwrapper.determine_economic_situation(red_team_players, round_economy[0],i, "RED")
                blue_team_econ = matchwrapper.determine_economic_situation(blue_team_players, round_economy[1],i, "BLUE")
                #step 4
                temp_kills = matchwrapper.get_all_kills_in_round(i)
                for y in temp_kills:
                    kill_tag = ""
                    #print(y.killer)
                    if y.timeSinceRoundStart<matchwrapper.get_round_plant_time(i):
                        kill_tag = "before plant"
                    else:
                        kill_tag = "after plant"
                    attacker_team = matchwrapper.get_player_team(y.killer)
                    victim_team = matchwrapper.get_player_team(y.victim)
                    for z in y.playerLocations:
                        #print("looking for attacker location")
                        if z.puuid == y.killer:
                            attacker_location = z.location
                            #print("found attacker location", type(attacker_location))
                    #step 5
                    vals = (queueId,rank,red_team_econ,blue_team_econ,attacker_team,victim_team,attacker_location.x,attacker_location.y,y.victimLocation.x,y.victimLocation.y,kill_tag)
                    mycursor.execute(sql, vals)
                    mydb.commit()
        test.close()

                #need to figure out how to get kill post or before plant maybe use the time stat but idk
                #get time of plant, kill object has time of death so just compare
                



                
                


if __name__ == "__main__":
    main()