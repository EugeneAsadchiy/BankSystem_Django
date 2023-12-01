# urls.py
from django.urls import path
from .views import apply_credit

urlpatterns = [
    # ... другие маршруты ...
    path('apply_credit/', apply_credit, name='apply_credit'),
]
