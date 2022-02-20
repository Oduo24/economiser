
from django.urls import path
from . import views
from .views import JanuaryView, FebruaryView, MarchView, AprilView, MayView, JuneView, JulyView, AugustView, \
    SeptemberView, OctoberView, NovemberView, DecemberView, DailyView, AnnualView, Year2018View, Year2021View


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/costcal', views.CostcalView, name="costcal"),
    path('index/meter', views.MeterReadingView, name='meter'),
    path('index/meter/consumption', views.ConsumptionView, name='consumption'),
    path('index/analyzer/01p', JanuaryView.as_view(), name='january'),
    path('index/analyzer/02p', FebruaryView.as_view(), name='february'),
    path('index/analyzer/03p', MarchView.as_view(), name='march'),
    path('index/analyzer/04p', AprilView.as_view(), name='april'),
    path('index/analyzer/05p', MayView.as_view(), name='may'),
    path('index/analyzer/06p', JuneView.as_view(), name='june'),
    path('index/analyzer/07p', JulyView.as_view(), name='july'),
    path('index/analyzer/08p', AugustView.as_view(), name='august'),
    path('index/analyzer/09p', SeptemberView.as_view(), name='september'),
    path('index/analyzer/10p', OctoberView.as_view(), name='october'),
    path('index/analyzer/11p', NovemberView.as_view(), name='november'),
    path('index/analyzer/12p', DecemberView.as_view(), name='december'),
    path('index/analyzer/000d', DailyView.as_view(), name='daily'),
    path('index/analyzer/000w', AnnualView.as_view(), name='annual'),
    path('index/analyzer/0000y018', Year2018View.as_view(), name='year2018'),
    path('index/analyzer/0000y021', Year2021View.as_view(), name='year2021'),





]










