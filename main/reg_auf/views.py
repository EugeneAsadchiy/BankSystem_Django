from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.models import User


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'reg_auf/registration.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reg_auf/login.html'

    def get_success_url(self):
        return reverse_lazy("main")


def logout_user(request):
    logout(request)
    return redirect("login")


def change_password(request):
    u = User.objects.get(username="arseniy")
    print(u.id)
    u.first_name = "butko"
    # u.set_first_name("butko")
    u.save()
    return render(request, 'base.html')


def main(request):
    return render(request, 'base.html')
