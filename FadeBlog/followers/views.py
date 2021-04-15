from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import UserFollowing
# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView,  CreateView, DeleteView, View

"""
class AddFollowerView(CreateView):
    model = UserFollowing

    def get_success_url(self):
        id = self.kwargs['id']
        return reverse(kwargs={'id': id})

    def post(self):
         UserFollowing.objects.create(user_id=User.id, following_user_id=self.kwargs['pk'])
"""


class Follow(CreateView):
    """ Добавление в подписчики"""
    success_url = reverse_lazy('an-user-post-list')

    def post(self, request, pk):
        user = User.objects.get(id=pk)
        UserFollowing.objects.create(following_user_id=request.user.id, user_id=user.id)


class UnFollow(CreateView):
    """Удаление подписчика"""
    success_url = reverse_lazy('an-user-post-list')

    def delete(self, request, pk):
        sub = UserFollowing.objects.get(following_user_id=request.user.id, user_id=pk)
        sub.delete()
