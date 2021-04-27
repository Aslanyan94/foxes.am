from django.urls import path, include
from .views import mad_views

urlpatterns = [
    path('', mad_views)
]
