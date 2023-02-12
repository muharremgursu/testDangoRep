from django.contrib import admin
from .models import Article, Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", 'created_date'] # Admin panelinde gösterilecek bilgileri seçme
    list_display_links = ['title', 'author', "created_date"] # Admin panelinde gösterilen bilgilerden hangileri tıklanabilir olacak?
    search_fields = ['title'] # Makale başlıklarına göre arama
    sortable_by = ['created_date', 'author'] # Makaleleri yazara göre ya da yayın tarihine göre sıralama
    list_filter = ['created_date']  # Tarihe göre makaleleri filtreleme
    class Meta():
        model = Article

""" Commnet modelini admin'e tanımlama """
admin.site.register(Comment)