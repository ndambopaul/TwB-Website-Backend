from django.db import models

from django.contrib.auth.models import AbstractUser
from apps.core.models import AbstractBaseModel

# Create your models here.
USER_ROLES = (
    ("Client", "Client"),
    ("Admin", "Admin"),
    ("Developer", "Developer"),
    ("Finance", "Finance"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=USER_ROLES, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True)

    def __str__(self):
        return self.username
