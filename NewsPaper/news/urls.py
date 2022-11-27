from django.urls import path, include
from .views import (PostDetail, NewsList, NewsFilter, NewsCreate, NewsDelete, NewsUpdate, PostDelete, PostCreate,
                    PostUpdate)

urlpatterns = [
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>/', PostDetail.as_view()),
    path('', NewsList.as_view()),
    path('search/', NewsFilter.as_view(), name='news_filter'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
