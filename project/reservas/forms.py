from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("Não é possível marcar para datas passadas.")
        return date
    
    def clean_time(self):
        time = self.cleaned_data['time']
        if time.hour < 12 or time.hour >= 23:
            raise forms.ValidationError("Horário deve ser entre 12:00 e 23:00.")
        return time