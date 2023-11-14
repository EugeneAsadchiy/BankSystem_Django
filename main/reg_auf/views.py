from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .forms import RegisterUserForm
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView


# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'reg_auf/registration.html'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    # success_url = reverse_lazy('/main')
    template_name = 'reg_auf/login.html'

    def get_success_url(self):
        return reverse_lazy("main")


def main(request):
    return HttpResponse("Главная страница")
