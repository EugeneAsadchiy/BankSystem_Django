# urls.py
from django.urls import path
from . import views


urlpatterns = [
    # ... другие маршруты ...
    path('apply_credit/', views.apply_credit, name='apply_credit'),
    path('apply_credit_successful/', views.apply_credit_successful, name='apply_credit_successful'),
    path('my_credits/', views.ListCredits.as_view(), name='my_credits'),
]
