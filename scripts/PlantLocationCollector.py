##similar to kill-deathcollector.py
##going to collect plant locations, rank, map and economy

## NEED TO FLIP TEAMS
import MatchWrapper
import MatchClasses
import json
import Constants
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=Constants.MYSQL_PASSWORD,
  database="whereidie"
)
def main():
    mycursor = mydb.cursor()
    
    for x in range(1):
        test = open(os.path.dirname(os.getcwd())+"/WhereIDie/testcases/match.json")
        match = MatchClasses.Match(json.load(test))
        matchwrapper = MatchWrapper.Match_Wrapper(match)
        sql = "INSERT INTO PLANT_LOCATIONS (queueid, mapid,rank_id, red_team_econ, blue_team_econ,location_x,location_y) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        mapId = match.matchinfo.mapId
        mapName = matchwrapper.get_map_name(mapId).upper()
        queueId = match.matchinfo.queueId
        rank = matchwrapper.get_avg_rank()
        if matchwrapper.get_num_of_rounds() >13 and matchwrapper.get_num_of_rounds() <19: #13-5 or less not counted
            continue
        for i in range(matchwrapper.get_num_of_rounds()):
            round_econ = matchwrapper.get_avg_economy(i)
            red_team_econ = matchwrapper.determine_economic_situation(match.teams[0].teamplayers,round_econ[0],i,"RED")
            blue_team_econ = matchwrapper.determine_economic_situation(match.teams[1].teamplayers,round_econ[1],i,"BLUE")
            plant_Location = matchwrapper.get_round_plant_location(i)
            val = (queueId,mapName,rank,red_team_econ,blue_team_econ,plant_Location.x,plant_Location.y)
            mycursor.execute(sql, val)
            mydb.commit()
    test.close()


if __name__ == "__main__":
    main()