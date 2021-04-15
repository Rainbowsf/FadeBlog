from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "published", "create_date",  "published", "view_count", "id")
# Register your models here.
