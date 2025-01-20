# core/forms.py
from django import forms
from .models import Contact, SignUp

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'subject': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'message': forms.Textarea(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'phone': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['name', 'email', 'phone', 'truck_type', 'trailer_size', 'mc_copy', 'noa', 'insurance_cert']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'phone': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'truck_type': forms.Select(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
            'trailer_size': forms.TextInput(attrs={'class': 'w-full bg-gray-800 rounded border border-gray-700 text-white'}),
        }