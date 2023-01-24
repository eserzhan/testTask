from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserModel(admin.ModelAdmin):
    list_display = ['created_at', 'username', 'email']


admin.site.register(User, UserModel)
