from django.urls import path
from . import views

app_name = "index"
urlpatterns = [
    path('' , views.articles_list, name="ind"),
    #path('<slug>' , views.articles_detail, name="detail"),
    
]
