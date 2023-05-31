from django.db import models

# Create your models here.
class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)    #поле которое хранит строку из N-символов
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=50)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'    #магический атрбут для красивого отображения в панели

    class Meta:
        verbose_name = 'Запись' #Используется для определения удобочитаемого единственного имени модели и заменяет стандартное соглашение об именах django
        verbose_name_plural = 'Записи' #Множественная часть

class Comments(models.Model):
    '''Комментарии'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=1000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE) #За счет каскада, если удалить пост, удалятся и все комменты к нему

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP-adress', max_length=50)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
