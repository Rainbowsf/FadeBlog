from . import views
from django.urls import path

urlpatterns = [
    path('', views.AccLoginView.as_view(), name='login'),
    path('logout/', views.AccLogoutView.as_view(), name='logout'),
]