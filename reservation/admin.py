from django.contrib import admin
from login.models import Profile
from .models import Spot,Reservation
# use 'python manage.py createsuperuser' to create superuser then can use /hostname/admin to look up all the registered models
'''
Username: xin
Email address: xin.kelly@hotmail.com
password:123456
'''
# Register your models here.

admin.site.register(Profile)
admin.site.register(Spot)
admin.site.register(Reservation)
