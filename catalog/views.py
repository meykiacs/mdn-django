from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_generes_contain_g = Genre.objects.filter(name__icontains='g').count()
    num_books_contain_b = Book.objects.filter(title__icontains='b').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_generes_contain_g': num_generes_contain_g,
        'num_books_contain_b': num_books_contain_b,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
