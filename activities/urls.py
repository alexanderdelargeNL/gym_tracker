# activities/urls.py
from django.urls import path
from .views import ActivityListView

urlpatterns = [
    path('', ActivityListView.as_view(), name='home'),
]