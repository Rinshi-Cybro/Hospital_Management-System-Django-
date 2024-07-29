from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class DateInput(forms.DateInput):
    input_type = 'date'
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        lables = {
            'patient_name': "Enter patient name:",
            'patient_phone': "Enter your phone number:",
            'patient_email': "Enter your email Id:",
            'doct_name': "Select a doctor:",
            'doct_department': "Select department:",
            'booking_date': "Select booking date:",
        } 




       
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout(
        #         Field('patient_name', css_class='form-control', placeholder='Enter patient name', label="Enter Patient Name"),
        #         Field('patient_phone', css_class='form-control', placeholder='Enter your phone number', label="Phone Number"),
        #         Field('patient_email', css_class='form-control', placeholder='Enter your email Id', label="Email"),
        #         Field('doct_name', css_class='form-control', label="Select Doctor"),
        #         Field('doct_department', css_class='form-control', label="Select Department"),
        #         Field('booking_date', css_class='form-control', label="Select Booking Date")
        #     )



           



        
        # lables = {
        #     'patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name', 'label':"Enter Patient Name"}),
        #     'patient_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        #     'patient_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email Id'}),
        #     'doct_name': forms.Select(attrs={'class': 'form-control'}),
        #     'doct_department': forms.Select(attrs={'class': 'form-control'}),
        #     'booking_date': DateInput(),
        # }

        
