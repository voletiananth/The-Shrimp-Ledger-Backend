from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from authentication.managers import UserManager


class User(AbstractUser):
    email = None
    username = None
    phone_number = models.BigIntegerField(unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.phone_number)

