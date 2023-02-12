from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def articles(request):
    keyword = request.GET.get('keyword')

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        context = {'articles':articles}
        return render(request, 'articles.html', context )

    articles = Article.objects.all()
    context = {"articles" : articles}
    return render(request, 'articles.html', context)

def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    """ Bu şekilde makaleler çekebiliyorduk ama aşağıdaki gibi 404 sayfası oluşturma fonksiyonu da kullanabiliriz."""
    """Article modelinden id'ye göre nesne çekiyor, bulamazsa da 404 sayfası gödneriyor."""
    article = get_object_or_404(Article, id=id)
    
    comments = article.comments.all()
    
    return render(request,'detail.html', {"article": article, 'comments':comments})

def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()
    
    return redirect('/articles/detail/'+str(id))
    #return redirect(reverse('article:detail', kwargs={'id':id}))

@login_required(login_url='/user/login/')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {"articles" : articles}
    return render(request, 'dashboard.html', context)

@login_required(login_url='/user/login/')
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makaleniz Eklendi")
        return redirect('index')
    
    return render(request, 'add_article.html', {'form':form})


@login_required(login_url='/user/login/')
def updateArticle(request, id):
    # Önce verilen id ile bir makale var mı kontrol edelim
    article = get_object_or_404(Article, id = id)
    # Ardından mevcut makale bilgileriyle formu sayfada göstereceğim
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Makale Güncellendi.')
        return redirect('index')
    
    return render(request, 'update.html', {'form':form})

@login_required(login_url='/user/login/')
def delete(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, 'Makaleniz silindi...')

    return redirect('dashboard')

