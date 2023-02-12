from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_article/', views.addArticle, name='add_article'),
    path('update/<int:id>', views.updateArticle, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('', views.articles, name='articles'),
    path('comment/<int:id>', views.addComment, name='comment'),
]
