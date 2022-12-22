from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Post, Category
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .filters import PostFilter
from datetime import datetime
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    model = Post  # Модель обьекта для вывода
    ordering = '-time_in'  # Поле, которое будет использоваться для сортировки объектов
    template_name = "news.html"  # Имя шаблона с инструкциями показа объекта пользователю
    context_object_name = 'post'  # Имя списка с объектами
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewsFilter(ListView):
    model = Post  # Модель обьекта для вывода
    ordering = '-time_in'  # Поле, которое будет использоваться для сортировки объектов
    template_name = "search.html"  # Имя шаблона с инструкциями показа объекта пользователю
    context_object_name = 'post'  # Имя списка с объектами

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('add_post',)
    raise_exception = True
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_detail')


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class PostUpdate(PermissionRequiredMixin, ListView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(PostCategory=self.category).order_by('-time_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})


class TestList(ListView):
    model = Post  # Модель обьекта для вывода
    ordering = '-time_in'  # Поле, которое будет использоваться для сортировки объектов
    template_name = "test.html"  # Имя шаблона с инструкциями показа объекта пользователю
    context_object_name = 'post'  # Имя списка с объектами
    paginate_by = 10
