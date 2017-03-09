
'''
This file is to define the model for User to registration and login.
New users create a new account using their email address, set up a password, and set up their phone number.
Registered user can use profile to login.

It creates a new Django Model called Profile to store the extra information(like phone number) and relates to the User Model using OneToOneField.
'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15,blank=False)


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()
