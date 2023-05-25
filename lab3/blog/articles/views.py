from django.shortcuts import render
from django.http import HttpResponse
from django import template


def home(request):
    return HttpResponse(u'Hello, World!', content_type="text/plain")

def archive(request):
    return render(request, 'archive.html')



#from models import Article
#from django.shortcuts import render

#def archive(request):
    #return render(request, 'archive.html', {"posts":
        #Article.objects.all()})
