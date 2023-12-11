from django.contrib.auth.models import AbstractUser
from django.db import models

from users.enums import UserRole


class UserYaMDb(AbstractUser):
    last_name = models.CharField(verbose_name='Фамилия', max_length=200)
    username = models.CharField(verbose_name='Имя пользователя', unique=True, max_length=200)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True, max_length=200)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    role = models.CharField(verbose_name='Роль', max_length=20, choices=UserRole.choices(), default=UserRole.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('last_name', 'first_name')

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN.value or self.is_superuser or self.is_staff

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR.value

    @property
    def is_user(self):
        return self.role == UserRole.USER.value
