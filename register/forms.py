from django import forms

class RegisterForm(forms.Form):
    profile_photo = forms.ImageField()
    resume = forms.FileField(required= False)