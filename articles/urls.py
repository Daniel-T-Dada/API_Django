from django.urls import path
from articles.views import (
    article_detail_view, 
    article_search_view, 
    article_create_view)

urlpatterns = [
    path('articles/', article_search_view, name='article-search'),  # Maps the article search view
    path('articles/create/', article_create_view, name='article-create'),  # Maps the article create view
    path('articles/<int:id>/', article_detail_view, name='article-detail'),  # Maps the article detail view
    # This URL pattern captures an integer 'id' from the URL and passes it to the article_detail_view function.
    # The name 'article-detail' can be used to refer to this URL in templates or redirects.
    # When a user accesses a URL like /articles/1/, the article with id 1 will be displayed.

    
]