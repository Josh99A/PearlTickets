from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User, BusSchedule


admin.site.register(User, UserAdmin)
admin.site.register(BusSchedule)




# Register your models here.
