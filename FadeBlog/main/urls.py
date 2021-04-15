from . import views
from django.urls import path

urlpatterns = [
    path('', views.StartPage.as_view(), name='start'),
    path('main/', views.HomePage.as_view(), name='home'),
    path('userlist/', views.UsersListView.as_view(), name='user_list'),
    path('userlist/<int:pk>', views.UsersDetailView.as_view(), name='user_detail'),
]
