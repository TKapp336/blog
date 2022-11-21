from django.shortcuts import render
from .models import Post # importing the database model Post
from django.views.generic import ListView, DetailView # import the ListView, DetailView class

# using a class-based view subclassing ListView
class BlogListView(ListView):
    # add our model
    model = Post
    # add our template
    template_name = "home.html"

class BlogDetailView(DetailView):
    # add our model
    model = Post
    # add our template
    template_name = "post_detail.html"
    
