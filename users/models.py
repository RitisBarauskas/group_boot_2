from django.contrib.auth.models import AbstractUser
from django.db import models


class UserYaMDb(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=200)
    last_name = models.CharField(verbose_name='Фамилия', max_length=200)
    username = models.CharField(verbose_name='Имя пользователя', unique=True, max_length=200)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

