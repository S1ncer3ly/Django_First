from django import forms
from django import views
from django.core.exceptions import ValidationError


class my_form(forms.Form):
    name = forms.CharField(label="Your Member_id", max_length=20)
    email = forms.EmailField(label="Your Email_id")
    course = forms.CharField(label="You Course_name", max_length=40)
    check = forms.BooleanField(label="Staff")
