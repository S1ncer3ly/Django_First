import requests
from django.shortcuts import render
from .form import my_form


# Create your views here.
def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def list(request):
    return render(request, "list.html")


def temp(request):
    return render(request, "template 1.html")


def forms(request):
    blank_form = my_form(request.POST or None)
    if blank_form.is_valid():
        Member_id = blank_form.cleaned_data.get("Name")
        email = blank_form.cleaned_data.get("email_add")
        course_id = blank_form.cleaned_data.get("course")
        chk = blank_form.cleaned_data.get("check")
        print("this is the member id ", Member_id)
        print("this is email_address", email)
        print("this is the course id", course_id)
        print("this is status of staff checkbox", chk)
    return render(request, "form.html", {"blank_form": blank_form})
