from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView,  CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from followers.models import UserFollowing

"""
class FollowersPostListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    template_name = "wall/wall-user-post-list.html"

    def get_queryset(self):
        return Post.objects.filter(
            user__in=self.request.user.id
        ).order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super(FollowersPostListView, self).get_context_data(**kwargs)
        context['follow_users'] = User.objects.filter(
            profile__in=self.request.user.id
        )
        return context
"""


class FollowersPostListView(LoginRequiredMixin, ListView):
    """ Список постов на стене пользователя"""
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    template_name = "wall/wall-user-post-list.html"
    context_object_name = "post_list"
    follower = UserFollowing.objects.filter(user_id=User.id)

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user')


class PostCreateView(LoginRequiredMixin, CreateView):
    """Создание постов через форму"""
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    form_class = PostForm
    template_name = 'wall/post-create.html'
    success_url = reverse_lazy('user-post-list')

    def form_valid(self, form):
        """Форма действительна, создается пост"""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """Ошибки в форме, редирект обратно в список постов"""
        print(form.errors)
        return redirect(reverse_lazy('user-post-list'))

    def post(self, *args, **kwargs):
        """Создание поста"""
        form = self.get_form()
        self.object = None
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserPostListView(LoginRequiredMixin, ListView):
    """Список постов авторизованного пользователя(моя страница)"""
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'wall/user-post-list.html'

    def get_queryset(self):
        return Post.objects.filter(
            user=self.request.user
        ).order_by('-create_date')


class AnotherUserPostListView(LoginRequiredMixin, ListView):
    """Список постов других пользователей"""
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    template_name = 'wall/an-user-post-list.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse('an-user-post-list', kwargs={'username': username})

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.kwargs['pk'])


class PostDetailView(LoginRequiredMixin, DetailView):
    """Просмотр конкретного поста"""
    login_url = '/login/'
    redirect_field_name = 'index.html'
    model = Post
    template_name = 'wall/post-detail.html'



