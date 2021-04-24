from django.urls import path, include
from .views import teams

urlpatterns = [
    path('', teams),
]


