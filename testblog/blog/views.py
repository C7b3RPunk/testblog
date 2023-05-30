from django.shortcuts import render
from django.views.generic.base import View   #Родительский класс, на базе которого будут писаться представления
from .models import Post   # откуда будем брать данные

# Create your views here. Все представления создаем тут

#субкласс от родительского класса View, где уже есть все механики
class PostView(View):
    '''Вывод записей'''
    def get(self, request):
        posts = Post.objects.all()  # подтягиваем всю инфу из Post
        return render(request, 'blog/blog.html', {'post_list': posts})  #Функция render которая объединяет шаблон со словарем(данные которые берем из модели) и возвращает объект httpResponse