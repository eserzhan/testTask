from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Order


class OrderModel(admin.ModelAdmin):
    list_display = ['created_at', 'status', 'profile', 'description']


admin.site.register(Order, OrderModel)
