from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'guests', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-date', '-time')