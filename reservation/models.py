from django.db import models
from login.models import Profile

# Create your models here.

# define the user model in login app and use the User model in django

# define the street parking spot model
class Spot(models.Model):
  spot_id = models.AutoField(primary_key=True)
  description = models.TextField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  cost_per_hour = models.FloatField()

# show spot's information
  def __str__(self):
    return self.description


# define the reservation model
class Reservation(models.Model):
  reservation_id = models.AutoField(primary_key=True)
  user = models.ForeignKey(Profile,on_delete=models.CASCADE,default=None)
  spot = models.ForeignKey(Spot,on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now=True) # only automatically updated when calling Reservation.save().
  duration = models.DurationField() # how long the reservation is
  paid_amount = models.FloatField()

  def __str__(self):
    return str(self.reservation_id)
