from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Yeni Makale Oluşturma Modeli
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar') # Django içindeki hazır user sınıfını kullandık
    title = models.CharField(max_length=50, verbose_name='Başlık')
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    article_image = models.FileField(blank=True, null=True, verbose_name='Görsel Ekle') # makalede görsel olmak zorunda değilse, blank ve null argümanlarını True yap

    def __str__(self):
        title = self.title
        author = self.author
        return title
    
    class Meta:
        ordering = ['created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Makale', related_name='comments')
    comment_author = models.CharField(max_length=50, verbose_name='İsim')
    comment_content = models.CharField(max_length=250, verbose_name='Yorum')
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']