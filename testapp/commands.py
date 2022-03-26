from testapp.models import Book, Author
from django.db.models import Count
from django.db import connection


def list_books():
    books = Book.objects.select_related().all()
    for book in books:
        print(f'"{book.title}".{book.author.name}')

def author_books():
    authors  = Author.objects.select_related().all()
    for author in authors:
        author_books = author.books.all()
        print(f'{author.name}: ',", ".join([f'"{book.title}"' for book in author_books]) )

def authors_rank():
    authors  = Author.objects.select_related() \
        .annotate(num_books=Count('books')) \
        .order_by('-num_books')
    for author in authors:
        author_books = author.books.all()
        print(f'{author.name}: ', f'{author.num_books}'  )


