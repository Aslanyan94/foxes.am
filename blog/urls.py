from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView, name="blog"),
    path('<int:_id>', BlogDetailView, name="blogs"),
]
