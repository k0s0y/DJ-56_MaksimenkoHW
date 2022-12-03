from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles_query = Article.objects.all()
    context = {
        'object_list': articles_query
    }

    return render(request, template, context)
