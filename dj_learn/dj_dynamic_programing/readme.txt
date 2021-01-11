there is a dynamicprogramming project

change in project and notes :

~>Step : 1

open root setting.py file 
NOTE: for jinja2 templating setting app

youtube link:
https://youtu.be/6zJo84q2blo?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=936

link:
https://stackoverflow.com/questions/30701631/how-to-use-jinja2-as-a-templating-engine-in-django-1-8

code part:
------------------------------------------------------------------------------
TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
        'OPTIONS': {'environment': 'myproject.jinja2.Environment',}, 
        
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
------------------------------------------------------------------------------


~>Step : 2

title: 
NOTE: 

youtube link:


stackoverflow link:


code part:
------------------------------------------------------------------------------

------------------------------------------------------------------------------


