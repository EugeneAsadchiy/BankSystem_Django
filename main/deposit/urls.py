# urls.py
from django.urls import path
from . import views


urlpatterns = [
    # ... другие маршруты ...
    # path('apply_credit/', views.apply_credit, name='apply_credit'),
    # path('apply_credit_successful/', views.apply_credit_successful, name='apply_credit_successful'),
    # path('my_credits/', views.ListCredits.as_view(), name='my_credits'),
    path('my_deposits/', views.ListDeposits.as_view(), name='my_deposits'),
    path('apply_deposit/', views.create_deposit, name='apply_deposit'),
    path('apply_deposit_successful/', views.success_url, name='apply_deposit_successful'),

]
