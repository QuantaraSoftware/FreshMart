from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Address

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone', 'address_line1', 'address_line2', 'landmark', 'city', 'state', 'pincode', 'is_default']
