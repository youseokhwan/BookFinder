from django.urls import path
from book.views import BookSearchView, BookInsertAndSearchView


app_name = 'book'
urlpatterns = [
    # root
    path('', BookSearchView.as_view(), name='index'),

    # 내 도서 추가
    path('insert/', BookInsertAndSearchView.as_view(), name='insert')
]
