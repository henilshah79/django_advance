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

title: config_id_attribute
~>new things in django i learn : 3


NOTE: 

youtube link: https://www.youtube.com/watch?v=K_NJZd-YsoU&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=47

referce link:

code part:
------------------------------------------------------------------------------
# here we got page source in browser
view-source:http://127.0.0.1:8000/

see the "forms" fields code
<tr>
  <th>
  <label for="id_name">Name:</label>
  </th>
  <td>
  <input type="text" name="name" required id="id_name">
  </td>
</tr>
<tr>
  <th>
  <label for="id_email">Email:</label>
  </th>
  <td>
  <input type="email" name="email" required id="id_email">
  </td>
</tr>


# config_id_attribute of forms fields
eg:
id="id_name", id="id_email"


{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    # normal form
    # fm = StudentRegistrationForm()

    # string with id
    # fm = StudentRegistrationForm(auto_id="some_%s")

    # fields with id
    # fm = StudentRegistrationForm(auto_id=True)

    # remove id
    # fm = StudentRegistrationForm(auto_id=False)

    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output in website(auto_id="some_%s")
<input type="text" name="name" required id="some_name"></td></tr>
<tr><th><label for="some_email">Email:</label></th><td><input type="email" name="email" required id="some_email">


output in website(auto_id=True)
<input type="text" name="name" required id="name"></td></tr>
<tr><th><label for="email">Email:</label></th><td><input type="email" name="email" required id="email">


output in website(auto_id=False)
<input type="text" name="name" required></td></tr>
<tr><th>Email:</th><td><input type="email" name="email" required>
------------------------------------------------------------------------------


title: config_lable_tags
~>new things in django i learn : 4


NOTE: 

youtube link: https://youtu.be/K_NJZd-YsoU?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=703

referce link:

code part:
------------------------------------------------------------------------------
{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    # lable suffix = ":"
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "=")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "A")
    fm = StudentRegistrationForm(auto_id=True, label_suffix = " ")
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output on website site
------------------------------------------------------------------------------

title: dynamic initial values
~>new things in django i learn : 5


NOTE: 

youtube link: https://youtu.be/K_NJZd-YsoU?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=881

referce link:

code part:
------------------------------------------------------------------------------
{% comment %} how to configure {% endcomment %}
views.py

def home(request):
    fm = StudentRegistrationForm(auto_id=True, label_suffix = " ", initial = {'name':"abc"})
    data ={
        "fm": fm,
    }
    return render(request, 'studentform.html', data)

output on website site
------------------------------------------------------------------------------

