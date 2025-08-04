from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from articles.models import Article
from random import randint
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# The purpose of the views.py is to render html web pages which are returned as responses to HTTP requests.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    
# OLD AND MANUAL METHOD 
        # # Handle the login logic here
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        
        
        # user = authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Invalid username or password"}
        #     return render(request, "accounts/login.html", context)
        
        
        if form.is_valid():
            user = form.get_user()  # Get the user object from the form
            login(request, user)  # Log the user in
            return redirect("home")  # Redirect to the home page after successful login
    else:
        # Render the login form
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)




def logout_view(request):
    if request.method == "POST":
        logout(request)  # Log the user out
        return render(request, "accounts/logout.html", context={})
    else:
        # Show logout confirmation page
        return render(request, "accounts/logout.html", context={})


def register_view(request):
    form = UserCreationForm(request.POST or None) 
    if form.is_valid():
        user_obj = form.save()
        return redirect("login")  # Redirect to the login page after successful registration
    
    context = {
        "form": form
    }
    # Render the registration form
    # If the form is valid, save the user and redirect to the login page
    # If the form is not valid, render the form with errors
    return render(request, "accounts/register.html", context=context)

def home_view(request, id=None, *args, **kwargs):
    """
    1. Take in a request(Django sends request to the view function).
    2. Return HTML as response.(Django sends response back to the browser).
    """
    
    if id is None:
        random_id = randint(1, 4)  # Generate a random integer between 1 and 4
    else:
        random_id = id  # Use the provided ID

    article_obj = Article.objects.get(id=random_id)  # Fetch an article object with id=random_id from the database
    article_title = article_obj.title  # Get the title of the article
    article_content = article_obj.content  # Get the content of the article
    article_author = article_obj.author  # Get the author of the article
    article_published_date = article_obj.published_date
    article_list = Article.objects.all()  # Fetch all articles from the database
    
    # my_list = [1, 2, 3, 4, 5]  # Example list to be used in the context
    # my_list = article_list

    context = {
        "id": article_obj.id,
        "title": article_title,
        "content": article_content,
        "name": article_author,
        "published_date": article_published_date,
        "article_list": article_list,
        "object_list": article_list,  # Adding the example list to the context
    }

    # Use render() to properly render the template with context
    return render(request, "home-view.html", context)
