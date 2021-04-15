from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post by {self.user}'