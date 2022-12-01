from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# We're subclassing the generic class-based view, CreateView in our SignUpView class. We specify the use of the built-in 
# UserCreationForm and the not-yet created template at signup.html. And we use reverse_lazy to redirect the user to the login
# page upon succesful registration
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
