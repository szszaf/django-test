from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.index, name='index'),
    path('authors', views.get_authors, name='authors'),
    path('authors/<int:author_id>/', views.get_author, name='author'),
]