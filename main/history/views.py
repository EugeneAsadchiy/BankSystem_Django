from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

# from .models import History
from history.models import History


class ListHistory(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "history/history_list.html"
    model = History  # само выберет все данные и передаст в контекст
    context_object_name = "histories"

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)



