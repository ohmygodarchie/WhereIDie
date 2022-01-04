##similar to kill-deathcollector.py
##going to collect plant locations, rank, map and economy
import MatchWrapper
import MatchClasses
import json
import Constants
import getinfo
import csv
import os
def main():
    for x in range(1):
        f = open(os.path.dirname(os.get_cwd())+"/testcases/outputs/plant_locations.csv","w")
        writer = csv.writer(f)
        test = open(os.path.dirname(os.get_cwd())+"/testcasesMatch.json")
        match = MatchClasses.Match(json.load(test))
        matchwrapper = MatchWrapper.Match_Wrapper(match)
        mapId = match.matchinfo.mapId
        queueId = match.matchinfo.queueId
        rank = matchwrapper.get_avg_rank()    
        if matchwrapper.get_num_of_rounds() >13 and matchwrapper.get_num_of_rounds() <19: #13-5 or less not counted
            continue
        for i in range(matchwrapper.get_num_of_rounds()):
            round_econ = matchwrapper.get_avg_economy(i)
            red_team_econ = matchwrapper.determine_economic_situation(match.teams[0].teamplayers,round_econ[0],i)
            blue_team_econ = matchwrapper.determine_economic_situation(match.teams[1].teamplayers,round_econ[1],i)
            plant_Location = matchwrapper.get_plant_location(i)




if __name__ == "__main__":
    main()