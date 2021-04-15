from django.contrib import admin
from .models import UserFollowing


@admin.register(UserFollowing)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user_id", "following_user_id")
