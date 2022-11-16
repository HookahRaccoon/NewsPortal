from django.urls import path, include
from .views import *

urlpatterns = [
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>/', PostDetail.as_view()),
   path('', NewsList.as_view()),
]