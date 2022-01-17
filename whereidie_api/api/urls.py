from django.urls import path
from . import views
urlpatterns = [
    path('getHelloWorld', views.index, name='index'),
    path('getHeatMap/<str:MAP>/<str:atk_econ>/<str:def_econ>', views.getHeatMap, name='getHeatMap'),
]