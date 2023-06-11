from django.urls import path
from . import views

app_name = "articles2"
urlpatterns = [
    path('' , views.articles_list, name="listt"),
    #path('<slug>' , views.articles_detail, name="detail"),
    
]
