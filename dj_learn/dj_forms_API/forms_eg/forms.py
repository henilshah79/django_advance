from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(initial="abc", help_text="this is a help_text demo")
    phno = forms.IntegerField()
    email = forms.EmailField()