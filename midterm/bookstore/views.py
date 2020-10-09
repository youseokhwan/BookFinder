from django.views.generic import TemplateView


class BookstoreView(TemplateView):
    template_name = 'bookstore/bookstore.html'
