from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class KorisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ime'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prezime'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'})
        }



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name', 'affected_brand', 'description', 'malicious_url', 
            'malicious_domain_registration_date', 'malicious_domain_dns_a', 
            'malicious_domain_dns_ns', 'malicious_domain_dns_mx', 
            'matching_keywords', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'affected_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Affected Brand'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'malicious_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Malicious URL'}),
            'malicious_domain_registration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'malicious_domain_dns_a': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNS A Record'}),
            'malicious_domain_dns_ns': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNS NS Record'}),
            'malicious_domain_dns_mx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNS MX Record'}),
            'matching_keywords': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Matching Keywords'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class RegisterUserForm(UserCreationForm):	

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


	def _init_(self, *args, **kwargs):
		super(RegisterUserForm, self)._init_(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
