from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Maintenance)
admin.site.register(MaintenanceDetail)
admin.site.register(WaterQuality)