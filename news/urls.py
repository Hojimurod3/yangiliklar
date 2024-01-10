from django.urls import path
from .views import news_simple,news_simple_a

urlpatterns = [
    path('simple/news1', news_simple),
    path('simple/news2',news_simple_a)
]
