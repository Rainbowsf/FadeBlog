from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse


class AccLoginView(LoginView):
    template_name = "account/login.html"


class AccLogoutView(LogoutView):
    pass




