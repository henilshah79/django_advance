from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def home(request):
    fm = StudentRegistrationForm()
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)