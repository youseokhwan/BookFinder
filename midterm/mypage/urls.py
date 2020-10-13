from django.urls import path
from mypage.views import BookLV, BookDV, BookAV, BookYAV


app_name = 'mypage'
urlpatterns = [
    # root
    path('', BookLV.as_view(), name='index'),

    # DetailView
    path('<str:pk>/', BookDV.as_view(), name='detail'),

    # ArchiveIndexView
    path('archive/year', BookAV.as_view(), name='year_search'),

    # YearArchiveView
    path('archive/<int:year>/', BookYAV.as_view(), name='year_archive')
]
