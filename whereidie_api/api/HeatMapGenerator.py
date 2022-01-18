#query sql database for map, queue, rank, and econ

#ASYNC is so hard might switch to sync
#remember to add offsets etc with the data (MAYBE DO THIS IN COLLECTORS)

from .scripts import Constants
import inspect
#from django.db import models
from . import models
from asgiref.sync import sync_to_async
def create_models(db_table):
    classvar = None
    if db_table == "kd_collector_ASCENT":
        classvar = models.KdCollectorAscent()
    elif db_table == "kd_collector_BIND":
        classvar = models.KdCollectorBind()
    elif db_table == "kd_collector_BREEZE":
        classvar = models.KdCollectorBreeze()
    elif db_table == "kd_collector_FRACTURE":
        classvar = models.KdCollectorFracture()
    elif db_table  == "kd_collector_SPLIT":
        classvar = models.KdCollectorSplit()
    elif db_table == "kd_collector_HAVEN":
        classvar = models.KdCollectorHaven()
    elif db_table == "kd_collector_ICEBOX":
        classvar = models.KdCollectorIcebox()
    else:
        print("Error: Invalid db_table")
        return
    return classvar

async def generate_heatmaps():
    list_of_models = inspect.getmembers(models)
    print(list_of_models) 
    for x in Constants.MAPS.values():
        db_table = "kd_collector_"+ x.upper()
        classvar = create_models(db_table)
        all_objs = await sync_to_async(classvar.objects.all)()
        for x in all_objs:
            print(x)
