from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView


class NewsList(ListView):
    model = Post  # Модель обьекта для вывода
    ordering = 'time_in'  # Поле, которое будет использоваться для сортировки объектов
    template_name = "news.html"  # Имя шаблона с инструкциями показа объекта пользователю
    context_object_name = 'post'  # Имя списка с объектами


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# class MyForm(FormView):
#     form_class = myForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         return super().form_valid(form)







# a = 'Nikita'

# def index(request):
#     return render(request, 'index.html', context={'name': a})

