from django.db import models

from apps.core.models import AbstractBaseModel


# Create your models here.
class Post(AbstractBaseModel):
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="post_images/", null=True)

    def __str__(self):
        return self.title


class PostComment(AbstractBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
