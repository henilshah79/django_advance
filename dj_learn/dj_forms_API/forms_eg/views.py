from django.shortcuts import render
from .forms import *
# Create your views here.

def home(request):
    # normal form
    # fm = StudentRegistrationForm()

    # string with id
    # fm = StudentRegistrationForm(auto_id="some_%s")

    # fields with id
    # fm = StudentRegistrationForm(auto_id=True)

    # remove id
    # fm = StudentRegistrationForm(auto_id=False)
    
    # lable suffix = ":"
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "=")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "A")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = " ")

    # dynamic initial values
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = " ", initial = {'name':"abc"})
    
    
    # field_order
    fm = StudentRegistrationForm(field_order=['name', 'email', 'phno'])

    fm_with_widget = Student_with_widget(initial={
        'name': 'Student'
    })




    data ={
        "fm": fm,
        "eg_widget":fm_with_widget
    }
    return render(request, 'studentform.html', data)