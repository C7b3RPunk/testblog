from django.shortcuts import render, redirect
from django.views.generic.base import View   #Родительский класс, на базе которого будут писаться представления
from .models import Post, Likes   # откуда будем брать данные
from .form import CommentsForm

# Create your views here. Все представления создаем тут

#субкласс от родительского класса View, где уже есть все механики
class PostView(View):
    '''Вывод записей'''
    def get(self, request):
        posts = Post.objects.all()  # подтягиваем всю инфу из Post
        return render(request, 'blog/blog.html', {'post_list': posts})  #Функция render которая объединяет шаблон со словарем(данные которые берем из модели) и возвращает объект httpResponse

class PostDetail(View):
    '''отдельная страница для записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComments(View):
    '''добавление комментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)  #Commit позволяет приостановить сохранение для редактирование данных или добавления новых
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DisLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')