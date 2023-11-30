from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("my_accounts/", views.ListAccounts.as_view(), name="my_accounts"),
    path("order_account_successful/", views.success_url, name="order_account_successful"),
    path("order_account/", views.create_account, name="order_account"),
    path('transfer/', views.transfer_view, name='transfer'),


]
