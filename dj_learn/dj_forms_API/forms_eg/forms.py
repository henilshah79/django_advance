from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()