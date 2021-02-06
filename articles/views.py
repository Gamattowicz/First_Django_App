from django.shortcuts import render
from articles.models import Article

def articles(request):
    return render(request, 'articles.html', {'articles' : Article.objects.all()})

def article(request, article_id):
    return render(request, 'article.html', {'article': Article.objects.get(id = article_id)})
