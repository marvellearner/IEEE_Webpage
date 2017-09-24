from django import forms
from .models import Register
from django.forms import ModelForm


class Submit(ModelForm):
    Address = forms.CharField(widget=forms.Textarea)
    Mobile_number = forms.IntegerField(label='Mobile Number' , error_messages= {'unique':'Mobile number already exists!!'})
    IEEE_mem_no = forms.CharField(label='IEEE Membership No.', error_messages= {'max_length':'Type an integer value of 8 digits'})

    class Meta:
        model = Register
        fields = ['Name', 'Email', 'Mobile_number', 'Address' , 'College' , 'IEEE_mem_no']

