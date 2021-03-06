#query sql database for map, queue, rank, and econ

#ASYNC is so hard might switch to sync
#remember to add offsets etc with the data (MAYBE DO THIS IN COLLECTORS)

from operator import indexOf
from .scripts import Constants
import inspect
#from django.db import models
from . import models
from asgiref.sync import sync_to_async
ranks = [[0],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],[24]]
rank_names = ["Unranked","Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Immortal", "Radiant"]
econ_types = {
    "Save": 0,
    "Pistol": 1,
    "Force": 2,
    "Half": 3,
    "Full": 4
}
# from enum import Enum
# class BuyType (Enum):
#     FULL = "Full"
#     HALF = "Half"
#     FORCE = "Force"
#     SAVE = "Save"
# class Map(Enum):
#     ASCENT = "Ascent"
#     BIND = "Bind"
#     BREEZE = "Breeze"
#     FRACTURE = "Fracture"
#     SPLIT = "Split"
#     HAVEN = "Haven"
#     ICEBOX = "Icebox"
#     def __str__(self):
#         return self.value

def create_models(db_table):
    classvar = None
    if db_table == "kd_collector_ASCENT":
        classvar = models.KdCollectorAscent.objects
    elif db_table == "kd_collector_BIND":
        classvar = models.KdCollectorBind.objects
    elif db_table == "kd_collector_BREEZE":
        classvar = models.KdCollectorBreeze.objects
    elif db_table == "kd_collector_FRACTURE":
        classvar = models.KdCollectorFracture.objects
    elif db_table  == "kd_collector_SPLIT":
        classvar = models.KdCollectorSplit.objects
    elif db_table == "kd_collector_HAVEN":
        classvar = models.KdCollectorHaven.objects
    elif db_table == "kd_collector_ICEBOX":
        classvar = models.KdCollectorIcebox.objects
    else:
        print("Error: Invalid db_table")
        return None
    return classvar

def generate_heatmaps():
    list_of_models = inspect.getmembers(models)
    for x in Constants.MAPS.values():
        db_table = "kd_collector_"+ x.upper()
        classvar = create_models(db_table)
        if classvar == None:
            continue
        for y in ranks:
            print(x,y)
            all_objs =  classvar.filter(rank_id__in=y) #change this to competitve but test is only unrated 
            # link for filter and more query stuff https://docs.djangoproject.com/en/4.0/ref/models/querysets/#id4
            rank_name = rank_names[indexOf(ranks,y)]
            for z in all_objs:
                if z.red_team_econ:
                    pass
                elif z.red_team_econ == "Force":
                    pass
                elif z.red_team_econ == "Half":
                    pass
                elif z.red_team_econ == "Full":
                    pass
                else:
                    print("Error: Invalid atk_econ")
                print(z)
