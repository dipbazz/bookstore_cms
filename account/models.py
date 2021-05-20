from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    class Meta:
        verbose_name = 'profile'
