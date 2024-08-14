from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Departments, Doctors
from django.contrib import messages
from .forms import BookingForm, ContactUsForm

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
    else:
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
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the same page to clear the form
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form})

# def success_view(request):
#     return render(request, 'success.html')


def department(request):
    dep_dict = {
        "dept" : Departments.objects.all()
    }
    return render(request, 'department.html', dep_dict)
