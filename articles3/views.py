
from django.shortcuts import render
from . import models 


# Create your views here.
def articles_list(request):
    articles = models.Article3.objects.all().order_by('date')

    args = {'articles3':articles}
    return render(request, 'articles3/sari.html' , args)


