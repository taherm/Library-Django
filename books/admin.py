from django.contrib import admin
from books.models import Book, Author, Publication, BookIssue

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(BookIssue)

# Register your models here.
