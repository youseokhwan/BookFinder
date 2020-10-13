from django.urls import path
from mypage.views import BookLV, BookDV, BookMAV


app_name = 'mypage'
urlpatterns = [
    # root
    path('', BookLV.as_view(), name='index'),

    # DetailView
    path('<str:pk>/', BookDV.as_view(), name='detail'),

    # MonthArchiveView
    path('<int:year>/<str:month>/', BookMAV.as_view(), name='book_month')
]
