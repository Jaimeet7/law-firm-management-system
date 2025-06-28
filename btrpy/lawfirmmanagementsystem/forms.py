from lawfirmmanagementsystem.models import Enquiry,Appointment
from django import forms

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

