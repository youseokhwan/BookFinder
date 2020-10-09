from django.urls import path
from book.views import BookView


app_name = 'book'
urlpatterns = [
    # root
    path('', BookView.as_view(), name='book')
]
