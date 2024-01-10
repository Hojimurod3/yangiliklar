from django.urls import path
from .views import news_simple,news_simple_a

urlpatterns = [
    path('simple/', news_simple),
    path('simple/a',news_simple_a)
]