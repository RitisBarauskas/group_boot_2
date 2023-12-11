from django.contrib.auth.models import AbstractUser
from django.db import models


class UserYaMDb(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')
