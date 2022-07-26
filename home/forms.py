from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        """
        Creates contact form
        """
        model = Contact
        fields = [
            'full_name',
            'email',
            'message',
        ]
