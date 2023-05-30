from django.urls import path
from . import views

#Пустые ковычки в path это главная страница
urlpatterns = [path('', views.PostView.as_view())]