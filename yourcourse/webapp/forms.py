from django import forms

from .models import contact

class contact_form(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('name', 'email', 'subject', 'contactMsg')
        labels = {
            'Full Name': "name",
            'email': "Email Address",
            'subject': "Subject",
            'contactMsg': "Message"
        }