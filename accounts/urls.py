# accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"), # we're using the view called SignUpView, which is a class-based
    # view since it has the .as_view() method attached to the endd
]