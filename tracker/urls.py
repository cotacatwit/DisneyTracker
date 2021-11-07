from django.urls import path
from .views import *

urlpatterns = [
    path('', TrackerView.as_view(), name='trackers_list_url')
]
