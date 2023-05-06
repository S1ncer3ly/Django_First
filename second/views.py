import requests
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from second.models import Post,Category
from .form import my_form


# Create your views here.
def index(request):
    return render(request, "index.html")


def home(request):
    # Loads Data from POSTS from db(10)
    posts=Post.objects.all()[:11]
    cats=Category.objects.all()
    #print(post)
    data={
        'posts':posts,
        'cats':cats
    }
    return render(request, 'home.html',data)


def list(request):
    return render(request, "list.html")


def temp(request):
    if request.method == 'POST':
        # get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send an email
        send_mail(
            f"New message from {name} ({email})",
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # redirect to a success page
        return render(request, 'success.html')

    # render the contact page template
    return render(request, 'template 1.html')


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

def post(request,url):
    post=Post.objects.get(url=url)
    return render(request,'posts.html',{'post':post})