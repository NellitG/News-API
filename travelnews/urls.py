from django.urls import path
from .views import get_travel_news, get_destinations
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/travel-news/', get_travel_news, name='travel-news'),
    path('api/destinations/', get_destinations, name='destinations'),
]