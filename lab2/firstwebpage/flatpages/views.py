from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.    
def home(request):
    return render(request, 'static_handler.html')

#def home(request):
    #return HttpResponse(u'Hello, World!', content_type="text/plain")