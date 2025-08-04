from turtle import home
from django.urls import path
from accounts.views import(
    home_view,
    login_view,
    logout_view,
    register_view
)

urlpatterns = [
    path('', home_view, name='home'),  # Maps the root URL to the home_view function
    path('accounts/login/', login_view, name='login'),  # Maps the login view
    path('accounts/logout/', logout_view, name='logout'),  # Maps the logout view
    path('accounts/register/', register_view, name='register'),  # Maps the register view
]
# This file defines the URL patterns for the accounts app.
# It includes a single URL pattern that maps the root URL to the home_view function.    
# When a user accesses the root URL of the accounts app, the home_view function will be called to handle the request and return an HTML response.