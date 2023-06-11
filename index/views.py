
from django.shortcuts import render
from . import models 


# Create your views here.
def articles_list(request):
    articles = models.Indexx.objects.all().order_by('date')

    args = {'index':articles}
    return render(request, 'index/index.html' , args)


