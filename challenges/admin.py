from django.contrib import admin
from django.db.models.aggregates import Min
from .models import First_Challenge, Second_Challenge

# Register your models here.
admin.site.register(First_Challenge)
admin.site.register(Second_Challenge)
