
from django.shortcuts import render
from . import models 


# Create your views here.
def articles_list(request):
    articles = models.Article2.objects.all().order_by('date')

    args = {'articles2':articles}
    return render(request, 'articles2/babol.html' , args)


