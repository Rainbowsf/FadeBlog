from . import views
from django.urls import path

urlpatterns = [
    path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    path('post/list/', views.UserPostListView.as_view(), name='user-post-list'),
    path('post/list/explore<int:pk>', views.AnotherUserPostListView.as_view(), name='an-user-post-list'),
    path('post/list/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.FollowersPostListView.as_view(), name='wall-user-post-list'),
]