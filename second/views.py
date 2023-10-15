from django.urls import reverse_lazy
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.views.generic import CreateView

from second.form import CommentForm
from second.models import Post, Category, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        cpassword = request.POST.get('pass2')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email address already exists.")
        else:
            my_user = User.objects.create_user(uname, email, password)
            my_user.save()
            messages.success(request, "User has been created successfully")
            return redirect('signin')  # Redirect to a different view after successful registration

    return render(request, "sign.html")


def signin(request):
    context = {}
    if request.method == 'POST':
        user = request.POST['username']  # Extract email from form data
        password = request.POST['password']  # Extract password from form data

        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['error_message'] = 'Invalid email or password'
            return render(request, 'sign.html', context)

    return render(request, 'sign.html', context)


def Logout(request):
    logout(request)
    return redirect('home')


def home(request):
    # Loads Data from POSTS from db(10)
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    # print(post)
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def list(request):
    return render(request, "list.html")


def contact(request):
    if request.method == 'POST':
        # get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # send an email
        send_mail(
            f"New message from {name} ({email})",
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # redirect to a success page
        return render(request, 'home.html')

    # render the contact page template
    return render(request, 'contact.html')


def post(request, url):
    posts = Post.objects.get(url=url)
    return render(request, 'posts.html', {'post': posts})


def categories(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    latest_categories = Category.objects.order_by('-add_date')[:5]  # Get the latest 5 categories
    i = 1
    return render(request, 'categories.html',
                  {'cat': cat, 'posts': posts, 'i': i, 'latest_categories': latest_categories})


def latest(request):
    posts = Post.objects.order_by('-add_date')[:5]  # Retrieve the latest 5 posts based on add_date
    categories = Category.objects.all()  # Retrieve all categories
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'home.html', context)


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, url=self.kwargs['url'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'url': self.kwargs['url']})
