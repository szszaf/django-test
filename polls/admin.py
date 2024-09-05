from django.contrib import admin
from polls.models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nationality', 'birth_date', 'image')
    search_fields = ('first_name', 'last_name')
    list_filter = ('nationality', )
    list_per_page = 10

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_per_page = 20
    list_filter = ('name', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'genre', 'author', 'publish_date', 'image')
    search_fields = ('isbn', 'title', 'genre', 'author')
    list_per_page = 20
    list_filter = ('genre', 'author')




