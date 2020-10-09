from django.views.generic import TemplateView


class BookView(TemplateView):
    template_name = 'book/book.html'
