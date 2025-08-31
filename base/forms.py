from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your college email'}))

class OTPForm(forms.Form):
    code  = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder':'Enter OTP'}))
class RegistrationForm(forms.Form):
    full_name      = forms.CharField(max_length=200)
    roll_number    = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=20)
    password       = forms.CharField(widget=forms.PasswordInput)
