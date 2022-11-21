# blog/urls.py
from django.urls import path
# we're importing the soon-to-be created views below.
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path("", BlogListView.as_view(), name="home"), # the empty string, "", tells Pythonto match all values and we make it
    # named URL, home
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # all blog entries will start with post/. Next is the
    # primary key for our post entry, which will be represented as an integer, <int:pk>. Django automatically adds an 
    # auto-incrementing primary key to our database models. So, while we only declared the fields title, author, and body on
    # our Post model, under-the-hood, Django also adds another field called id, which is our primary key. If you look back 
    # to the get_absolute_url method on our Post model, it passes in a pk argument because the URL here requires it. 
]