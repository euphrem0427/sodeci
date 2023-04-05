from django.contrib import admin
from .models import User, StatusHistory
# Register your models here.

admin.site.register(User)
admin.site.register(StatusHistory)
