from django.contrib import admin

from .models import UserYaMDb


@admin.register(UserYaMDb)
class UserYaMDbAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
    search_fields = ('username',)
    list_filter = ('role',)
    empty_value_display = '-пусто-'
