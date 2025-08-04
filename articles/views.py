from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.


def article_search_view(request):

    # print(request.GET)
    query_dict = request.GET # This is a dictionary-like object containing all GET parameters
    # query = query_dict.get("q")
    
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
        try:
            # Attempt to retrieve the article by ID
            article_obj = Article.objects.get(id=query)
        except Article.DoesNotExist:
            article_obj = None  # Handle the case where the article does not exist
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)




@login_required 
def article_create_view(request):
    # This view is for creating a new article
    form = ArticleForm(request.POST or None)  
    context = {
        "form": form
    }
    
        
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()  # Reset the form after successful submission
        # This will clear the form fields after submission
        context['object'] = article_object
        context['created'] = True
    return render(request, "articles/create.html", context=context)




# def article_create_view(request):
#     # This view is for creating a new article
#     form = ArticleForm()
    
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
        
#         context['form'] = form
        
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")

#             print(title, content)  # Debugging output to check the received data
#             article_object = Article.objects.create(title=title, content=content)

#             context['object'] = article_object
#         # You can also add more context if needed, like:
#             context['title'] = title
#             context['content'] = content
#             context['created'] = True
#         # Redirect to a success page or the article detail view after creation
#         # return render(request, "articles/create_success.html", context={"title": title})
    

#     return render(request, "articles/create.html", context=context)



def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        'object': article_obj,
    }

    return render(request, "articles/detail.html", context=context)
