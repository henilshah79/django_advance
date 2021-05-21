from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(initial="abc", help_text="this is a help_text demo")
    phno = forms.IntegerField()
    email = forms.EmailField()


class Student_with_widget(forms.Form):
    name = forms.CharField(
        label="Your name", 
        initial="abc",
        label_suffix=" ",
        required=False,
        disabled=True,
        help_text="this is a help_text demo",
    )
