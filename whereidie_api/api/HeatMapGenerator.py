#query sql database for map, queue, rank, and econ

#ASYNC is so hard might switch to sync
#remember to add offsets etc with the data (MAYBE DO THIS IN COLLECTORS)

from .scripts import Constants
import inspect
#from django.db import models
from . import models
from asgiref.sync import sync_to_async
from enum import Enum
class BuyType (Enum):
    FULL = "Full"
    HALF = "Half"
    FORCE = "Force"
    SAVE = "Save"
class Map(Enum):
    ASCENT = "Ascent"
    BIND = "Bind"
    BREEZE = "Breeze"
    FRACTURE = "Fracture"
    SPLIT = "Split"
    HAVEN = "Haven"
    ICEBOX = "Icebox"
    def __str__(self):
        return self.value
class Rank(Enum):
    pass
    # 3 -> "Iron 1"
    # 4 -> "Iron 2"
    # 5 -> "Iron 3"
    # 6 -> "Bronze 1"
    # 7 -> "Bronze 2"
    # 8 -> "Bronze 3"
    # 9 -> "Silver 1"
    # 10 -> "Silver 2"
    # 11 -> "Silver 3"
    # 12 -> "Gold 1"
    # 13 -> "Gold 2"
    # 14 -> "Gold 3"
    # 15 -> "Plat 1"
    # 16 -> "Plat 2"
    # 17 -> "Plat 3"
    # 18 -> "Diamond 1"
    # 19 -> "Diamond 2"
    # 20 -> "Diamond 3"
    # 21 -> "Immortal 1"
    # 22 -> "Immortal 2"
    # 23 -> "Immortal 3"
    # 24 -> "Radiant"
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
        return
    return classvar

def generate_heatmaps():
    list_of_models = inspect.getmembers(models)
    print(list_of_models) 
    for x in Constants.MAPS.values():
        db_table = "kd_collector_"+ x.upper()
        classvar = create_models(db_table)
        if classvar == None:
            continue
        all_objs =  classvar.all()
        for x in all_objs:
            print(x)
