from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    The form is for user to contact the shop owner.
    """
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'message',
        ]
