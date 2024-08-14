from django import forms
from .models import Booking, ContactUs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Row, Column, Submit


class DateInput(forms.DateInput):
    input_type = 'date'


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'  
        widgets = {
            'message': forms.Textarea(attrs={'rows': 2}),

            # 'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            # 'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            # 'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            # 'city': forms.TextInput(attrs={'placeholder': 'Enter ur city'}),
            # 'select_doctor': forms.Select(attrs={'placeholder': 'Select ur doctor'}),
            # 'select_department': forms.Select(attrs={'placeholder': 'Select ur department'}),

        } 

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('select_doctor', css_class='form-group col-md-6 mb-0'),
                Column('select_department', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'message',
            Submit('submit', 'SUBMIT FORM', css_class='btn')
        )    
        
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        # widgets = {
        #     'patient_name': forms.TextInput(attrs={'placeholder': 'Enter patient name'}),
        #     'patient_phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        #     'patient_email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        #     'doct_name': forms.Select(attrs={'placeholder': 'Select ur doctor'}),
        #     'doct_department': forms.Select(attrs={'placeholder': 'Select ur department'}),
        #     'booking_date': DateInput(),
        # } 

        
