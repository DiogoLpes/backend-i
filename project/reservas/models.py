from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"