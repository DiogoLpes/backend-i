from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    model = Reservation
    fields = ['name', 'phone', 'table', 'date', 'time', 'num_people', 'num_children', 'preferred_location']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.TimeInput(attrs={'type': 'time'}),
    }
