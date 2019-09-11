from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationFrom, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','num_bags', 'is_staff', ]

admin.site.register(CustomUser, CustomUserAdmin)
