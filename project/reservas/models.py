from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=20, choices=[
        ('inside', 'Inside'),
        ('outside', 'Outside')
    ])
    
    def __str__(self):
        return f"Table {self.number} ({self.location})"

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    children = models.IntegerField(default=0)
    preferred_location = models.CharField(max_length=10, choices=[
        ('inside', 'Inside'),
        ('outside', 'Outside')
    ])
       
    
    def __str__(self):
        return f"Reservation by {self.name} for {self.date} at {self.time}"