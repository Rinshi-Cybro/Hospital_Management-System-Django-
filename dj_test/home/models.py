from django.db import models

# Create your models here.


class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    


class Doctors(models.Model):
    doct_name = models.CharField(max_length=50)
    doct_specialization = models.CharField(max_length=100)
    doct_department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    doct_image = models.ImageField(upload_to='doctors_pic', blank=True, null=True)  

    def __str__(self):
        return self.doct_name



class Booking(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_phone = models.IntegerField()
    patient_email = models.EmailField()
    doct_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    doct_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    booking_date = models.DateField(null=True, blank=True)
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.patient_name
    


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    select_doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    select_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    message = models.TextField() 

    def __str__(self):
        return self.full_name  