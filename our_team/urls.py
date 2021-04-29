from django.urls import path, include
from .views import mad_views,les_views,young_views,old_views

urlpatterns = [
    path('mad', mad_views),
    path('les', les_views),
    path('young', young_views),
    path('old', old_views)
]
