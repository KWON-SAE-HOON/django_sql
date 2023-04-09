from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from . form import ArticleForm

from . models import Article
# Create your views here.


@require_safe
def index(request):
    articles = Article.objects.all()

    return render(request, 'blog/index.html', {
        'articles' : articles
    })

@require_safe
def detail(request, article_pk):
    article = get_object_or_404(pk=article_pk)
    return render(request, 'blog/detail.html', {
        article : article,
    })
    
@require_http_methods(['POST', 'GET'])
def create(request):

    if request == 'POST':
        form = ArticleForm(request.post)
        if form.is_valid:
            article = form.save()
            
            return redirect('blog:detail', article.pk)
        
    else:
        form = ArticleForm()

        return render(request, 'blog/form.html', {
            'form' : form,
        })
            