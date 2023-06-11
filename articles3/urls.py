from django.urls import path
from . import views

app_name = "articles3"
urlpatterns = [
    path('' , views.articles_list, name="listtt"),
    #path('<slug>' , views.articles_detail, name="detail"),
    
]
