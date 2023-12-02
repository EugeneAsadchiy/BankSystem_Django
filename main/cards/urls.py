from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("reg/", views.RegisterUser.as_view(), name="register"),
    # path("login/", views.LoginUser.as_view(), name="login"),
    # path("main/", views.main, name="main"),
    # path("logout/", views.logout_user, name="logout"),
    # path("order_card/", views.order_card, name="order_card"),
    # path("order_card/", views.CardView.as_view(), name="order_card"),
    path("my_cards/", views.ListCards.as_view(), name="my_cards"),
    path("order_card_successful/", views.success_url, name="order_card_successful"),
    path("order_card_debit/", views.create_card_debit, name="order_card_debit"),
    path("order_card_credit/", views.create_card_credit, name="order_card_credit"),


]
