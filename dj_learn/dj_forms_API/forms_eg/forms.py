from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(initial="abc", help_text="this is a help_text demo")
    phno = forms.IntegerField()
    email = forms.EmailField()


class Student_with_args(forms.Form):
    name = forms.CharField(
        label="Your name", 
        initial="abc",
        label_suffix=" ",
        required=False,
        disabled=True,
        help_text="this is a help_text demo",
    )

class Student_with_widget(forms.Form):
    name = forms.CharField(
        widget = forms.HiddenInput
    )
    passwd = forms.CharField(
        widget = forms.PasswordInput(),
    )

    textarea = forms.CharField(
        widget = forms.Textarea()
    )
    
    NumberInput = forms.CharField(
        widget = forms.NumberInput()
    )

    EmailInput = forms.CharField(
        widget = forms.EmailInput()
    )

    URLInput = forms.CharField(
        widget = forms.URLInput()
    )

    DateInput = forms.CharField(
        widget = forms.DateInput()
    )

    DateTimeInput = forms.CharField(
        widget = forms.DateTimeInput()
    )

    TimeInput = forms.CharField(
        widget = forms.TimeInput()
    )

    Select = forms.CharField(
        widget = forms.Select()
    )

    # NullBoolenSelect = forms.CharField(
    #     widget = forms.NullBoolenSelect()
    # )


    # selectMultiple = forms.CharField(
    #     widget = forms.selectMultiple()
    # )

    RadioSelect = forms.CharField(
        widget = forms.RadioSelect()
    )

    CheckboxSelectMultiple = forms.CharField(
        widget = forms.CheckboxSelectMultiple()
    )

    FileInput = forms.CharField(
        widget = forms.FileInput()
    )

    MultipleHiddenInput = forms.CharField(
        widget = forms.MultipleHiddenInput()
    )

    SplitDateTimeWidget = forms.CharField(
        widget = forms.SplitDateTimeWidget()
    )

    SplitHiddenDateTimeWidget = forms.CharField(
        widget = forms.SplitHiddenDateTimeWidget()
    )

    # SplitDateWidget = forms.CharField(
    #     widget = forms.SplitDateWidget()
    # )
     
    text_with_attrs = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'somecss',
            'id':'uniqueid'
        })
    )


class StudentRegistrationForm_demo(forms.Form):
    name = forms.CharField(initial='abc')
    phno = forms.IntegerField(initial='123')
    email = forms.EmailField(initial='abc@gmail.com')
    passwd = forms.CharField(widget=forms.PasswordInput())

