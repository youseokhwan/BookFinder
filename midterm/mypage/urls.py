from django.urls import path
from mypage.views import MypageView


app_name = 'mypage'
urlpatterns = [
    # root
    path('', MypageView.as_view(), name='index')
]
