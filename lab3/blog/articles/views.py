from django.shortcuts import render
from articles.models import Article
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
