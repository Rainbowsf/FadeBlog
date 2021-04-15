from django.shortcuts import render
from django.contrib.auth.models import User
from django.apps import apps
from django.views.generic import TemplateView, DetailView, ListView



class StartPage(TemplateView):
    template_name = "main/index.html"


class HomePage(TemplateView):
    template_name = "main/home_page.html"


class UsersListView(ListView):
    model = User
    context_object_name = 'profile_list'
    template_name = 'main/profile_list.html'


class UsersDetailView(DetailView):
    model = User
    context_object_name = 'profile_page'
    template_name = 'main/profile_page.html'