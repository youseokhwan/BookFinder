from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from book.models import Book


class BookLV(ListView):
    model = Book
    template_name = 'mypage/book_list.html'
    paginate_by = 6


class BookDV(DetailView):
    model = Book
    template_name = 'mypage/book_detail.html'


class BookAV(ArchiveIndexView):
    model = Book
    template_name = 'mypage/book_year_search.html'
    date_field = 'pubdate'
    allow_empty = True


class BookYAV(YearArchiveView):
    model = Book
    template_name = 'mypage/book_archive_year.html'
    date_field = 'pubdate'
    make_object_list = True
    paginate_by = 6