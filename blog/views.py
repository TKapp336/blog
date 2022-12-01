from django.shortcuts import render
from .models import Post # importing the database model Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # import the ListView, DetailView class,
# CreateView class, UpdateView class, DeleteView class
from django.urls import reverse_lazy # for redirects after deleting blog posts

# using a class-based view subclassing ListView
class BlogListView(ListView):
    # add our model
    model = Post
    # add our template
    template_name = "home.html"

# in this new view, we define the model we're using, post, and the template we want it associated with, post_detail.html
# by default, DetailView will provide a context object we can use in our template called either object or the lowercased
# name of our model, which would be post. Also, DetailView expects either a primary key or a slug passed to it as the
# identifier.
class BlogDetailView(DetailView):
    # add our model
    model = Post
    # add our template
    template_name = "post_detail.html"

# view to create a new blog; import the generic (Django built-in) CreateView class at the top of the page, and then subclass it
# to create a new view called BlogCreateView. In this view we specify our database model, Post, the name of our template, 
# post_new.html, and explicitly set the database fields we want to expose, which are title, author, and body
class BlogCreateView(CreateView):
    # add our model
    model = Post
    # add our template
    template_name = "post_new.html"
    # specify fields to edit
    fields = ["title","author","body"]

# a view to allow the user to update/edit a blog post. Notice that we are explicitly listing the fields we want to use 
# ["title", "body"] rather than using the __all__ method. This is because we assume that the author of the post is not 
# changing; we only want the title and text to be editable.
class BlogUpdateView(UpdateView):
    # add our model
    model = Post
    # add our template
    template_name = "post_edit.html"
    # specify fields to edit
    fields = ["title","body"]

# delete blogs subclassing the DeleteView generic built-in Django class
class BlogDeleteView(DeleteView):
    # add our model
    model = Post
    # specify our template
    template_name = "post_delete.html"
    # redirect to the home page after a blog post is deleted
    success_url = reverse_lazy("home")

