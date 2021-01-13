from django.shortcuts import render

# Create your views here.
def home(reuqest):
    context = {
        'nm':'django'
    }
    return render(reuqest, 'index.html', context)