from django.urls import path, include
from .views import (PostDetail, NewsList, NewsFilter, NewsCreate, NewsDelete, NewsUpdate, PostDelete, PostCreate,
                    PostUpdate, CategoryListView, TestList, subscribe)

urlpatterns = [
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>/', PostDetail.as_view(), name='post_list'),
    path('', NewsList.as_view(), name='post_detail'),
    path('search/', NewsFilter.as_view(), name='news_filter'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('test/', TestList.as_view(), name='test')
]
