
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/costcal', views.CostcalView, name="costcal"),
    path('index/meter', views.MeterReadingView, name='meter'),
    path('index/meter/consumption', views.ConsumptionView, name='consumption'),



]










