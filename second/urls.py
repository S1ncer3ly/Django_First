"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import include, path
from second import views
from second.views import CommentView

urlpatterns = [
    path("", views.home, name="index"),
    path("home", views.home, name="home"),
    path("about", views.list, name="about"),
    path("contact", views.contact, name="contact us"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name='signup'),
    path("logout", views.Logout, name='Logout'),
    path("<slug:url>", views.post, name="post"),
    path('category/<slug:url>/', views.categories, name='category'),
    path('accounts/', include('allauth.urls')),
    path('<slug:url>/comment/', CommentView.as_view(), name='comment'),
]
