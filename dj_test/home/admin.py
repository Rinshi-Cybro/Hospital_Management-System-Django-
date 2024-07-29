from django.contrib import admin
from .models import Departments, Doctors, Booking

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):
    booking_display = ('id', 'patient_name',  'patient_phone', 
                       'patient_email', 'doct_name', 'doct_department', 'booking_date', 'booked_on')
    
admin.site.register(Booking, BookingAdmin)