from django.urls import path
from bookstore.views import BookstoreView


app_name = 'bookstore'
urlpatterns = [
    # root
    path('', BookstoreView.as_view(), name='index')
]
