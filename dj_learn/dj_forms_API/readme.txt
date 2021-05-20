title: forms API
~>new things in django i learn : 1


NOTE:

youtube link: https://www.youtube.com/watch?v=CtD4u-Bncf8&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=47


referce link:

code part:
------------------------------------------------------------------------------
forms.py
--------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

---------
views.py
---------

from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def home(request):
    fm = StudentRegistrationForm()
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

----------------
studentform.html
----------------

<!doctype html>
<html lang="en">
  <head>
    <title>student</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  <body>
      <form action="" method="post">
          <table>
              {{fm}}
              <tr>
                  <th>
                      <button type="submit">submit</button>
                  </th>
              </tr>
          </table>
      </form>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
------------------------------------------------------------------------------


title: forms render options
~>new things in django i learn : 2


NOTE: here the "forms" is a simple example

youtube link: https://youtu.be/CtD4u-Bncf8?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=1863

referce link:

code part:
------------------------------------------------------------------------------
1. render all data
{{forms}}

2. as_table <tr> tag
{{forms.as_table}}

3. as_p <p> tag
{{forms.as_p}}

4. as_ul
{{forms.as_ul}}

5. field name manually
{{forms.name_of_field}}

eg.
forms.py
--------
from django import forms


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


{{forms.name}}
{{forms.email}}
------------------------------------------------------------------------------