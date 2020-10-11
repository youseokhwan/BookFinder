from django.urls import path
from book.views import BookSearchView


app_name = 'book'
urlpatterns = [
    # root
    path('', BookSearchView.as_view(), name='index')
]
