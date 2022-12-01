# At the top, we’re importing the class models and...
from django.db import models
# the handy utility function reverse that allows us to reference an object by its URL template name.
from django.urls import reverse

# Assume that each post has a title, author, and body.
# We create subclass of models.Model, called Post, which provides everythin with django.db.models.Models.
class Post(models.Model):
    # Then, we can add additional fields as desired.
    # Our model has three fields:
    # title, which is limited to a length of 200 characters
    title = models.CharField(max_length=200)
    # author, which is a foreign key that follows a many to one relationship (an author can have one to many posts,
    # but not the other way around); the reference is to the built in User model that Django provides for authentication;
    # for all many-to-one relationships, such as ForeignKey, we must also specify an on_delete option
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    # body, which uses a TextField to automatically expand as needed to fit the user's text
    body = models.TextField()

    # a __str__ method is added to provide a human readable version of the model in the admin or Django shell
    def __str__(self):
        # returning the title
        return self.title

    # this method tells Django how to calculate the canonical URL for our model object; it says to use the URL named
    # post_detail and pass in the pk. 
    def get_absolute_url(self):
        return reverse("home")