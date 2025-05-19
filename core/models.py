from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_passenger = models.BooleanField(default=True)
    is_bus_admin = models.BooleanField(default=False)
    
    
class BusSchedule(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    date = models.DateField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    bus_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.origin} to {self.destination} on {self.date}"
     



