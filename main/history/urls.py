# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('my_history/', views.ListHistory.as_view(), name='my_history'),
]
