from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Departments, Doctors
from .forms import BookingForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def booking(request):
    if request.method == 'POST':
        form_obj = BookingForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            # return render(request, 'booking.html')

    form = BookingForm()
    form_dict = {
        'form': form
    }
    return render(request, 'booking.html', form_dict)


def doctors(request):
    doct_dict = {
        "doctors" : Doctors.objects.all()
    }
    return render(request, 'doctor.html', doct_dict)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dep_dict = {
        "dept" : Departments.objects.all()
    }
    return render(request, 'department.html', dep_dict)
