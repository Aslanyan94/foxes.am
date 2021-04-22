from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView, name="blogs"),
    path('<int:_id>', BlogDetailView, name="blog"),
]
