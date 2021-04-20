from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .models import Freelancer

class FreelancerForm(forms.ModelForm):
        phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}), 

                       label=_("Phone number"), required=False)
        class Meta:
            model = Freelancer
            fields = ("name","url","phone")
    
    
