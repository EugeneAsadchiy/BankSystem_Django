from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("reg/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path("main/", views.main, name="main"),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path("change_password/", views.change_password, name="change_password"),
    # path('change_password/', PasswordChangeView.as_view(template_name='registration/change_password.html'),
    #      name='change_password'),
    path("logout/", views.logout_user, name="logout"),

]
