from django.contrib import admin
from django.contrib.auth.models import User
from .models import Registered_Users, UserOTP

# Register your models here.

admin.site.register(Registered_Users)
admin.site.register(UserOTP)