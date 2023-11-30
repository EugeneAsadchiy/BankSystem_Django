from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import request
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.models import User


# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('change-password-success')
    template_name = "reg_auf/change-password.html"


def password_success(request):
    return render(request, 'reg_auf/change-password-success.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'reg_auf/registration.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reg_auf/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Вы успешно вошли в систему!')
        return reverse_lazy("main")


@login_required(login_url='login')  # Обеспечивает, что пользователь авторизован
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Перенаправление на профиль после успешного редактирования
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'reg_auf/edit_profile.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("login")


# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Обновление сессии после смены пароля
#             return redirect('change_password_success')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {'form': form})


def main(request):
    return render(request, 'base.html')
