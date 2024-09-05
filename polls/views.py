from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from .models import Author, Book


def index(request):
    return render(request, 'polls/index.html', {'extra_text': 'hello, world'})

def get_authors(request):
    name = request.GET.get('name', None)
    if name is None:
        # return HttpResponse(
        #     serializers.serialize('json', Author.objects.all()))
        return render(request, 'polls/authors.html', {'authors': Author.objects.all()})
    else:
        return HttpResponse(
            serializers.serialize('json', Author.objects.filter(last_name__exact=name)))

# def get_author(request, author_id):
#     author = [Author.objects.get(pk=author_id)]
#     print(request.accepted_types)
#     return HttpResponse(
#         serializers.serialize('json', author))

def get_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author_books = Book.objects.filter(author=author)
    return render(request, 'polls/author.html',
                  {'author': author, 'author_books': author_books})

