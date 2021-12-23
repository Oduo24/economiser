
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView, name='index'),
    path('index/costcal', views.CostcalView, name="costcal"),


]










