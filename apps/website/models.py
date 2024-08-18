from django.db import models

from apps.core.models import AbstractBaseModel


# Create your models here.
class Team(AbstractBaseModel):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=255, choices=(("Male", "Male"), ("Female", "Female"))
    )
    email = models.EmailField()
    linkedin = models.URLField(null=True)
    github = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="team_images/", null=True)
    about_me = models.TextField(null=True)

    def __str__(self):
        return self.name


class Testimonial(AbstractBaseModel):
    recorded_by = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.author


class Message(AbstractBaseModel):
    author = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    message_type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Client(AbstractBaseModel):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    date_signed = models.DateField(null=True)
    logo = models.ImageField(upload_to="client_logos/", null=True)

    def __str__(self):
        return self.name
