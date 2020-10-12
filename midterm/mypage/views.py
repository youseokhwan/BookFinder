from django.views.generic import ListView, DetailView, MonthArchiveView
from book.models import Book


class BookLV(ListView):
    model = Book
    template_name = 'mypage/book_list.html'
    paginate_by = 6


class BookDV(DetailView):
    model = Book
    template_name = 'mypage/book_detail.html'


class BookMAV(MonthArchiveView):
    model = Book
    template_name = 'mypage/book_archive_month.html'
    date_field = 'pubdate'
    make_object_list = True