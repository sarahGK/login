from django.contrib import admin
from login.models import Profile
from .models import Spot,Reservation

# Register your models here.

admin.site.register(Profile)
admin.site.register(Spot)
admin.site.register(Reservation)
