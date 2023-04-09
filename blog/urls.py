
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.index , name='index'),
    # blog/1/detail/
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    # blog/create/
    path('create/', views.create, name='create')


]
