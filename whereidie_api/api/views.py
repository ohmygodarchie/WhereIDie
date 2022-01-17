from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import asyncio
import httpx
from .scripts import getinfo
from .scripts import Constants
# Create your views here.
#just a hello world func

api = getinfo.apihandler()
async def index(request):
    return HttpResponse("hello world")


#compile heatmap data
async def getHeatMap(request,MAP, atk_econ, def_econ):
    if MAP not in Constants.MAPS.values():
        return HttpResponseNotFound('404 Not Found')
    if atk_econ not in ["Save", "Force", "Half", "Full"]:
        return HttpResponseNotFound('404 Not Found')
    if def_econ not in ["Save", "Force", "Half", "Full"]:
        return HttpResponseNotFound('404 Not Found')
    
    return HttpResponse(MAP)
