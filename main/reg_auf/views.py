from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'reg_auf/registration.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    # success_url = reverse_lazy('/main')
    template_name = 'reg_auf/login.html'

    def get_success_url(self):
        return reverse_lazy("main")


def logout_user(request):
    logout(request)
    return redirect("login")


def main(request):
    return render(request, 'base.html')
