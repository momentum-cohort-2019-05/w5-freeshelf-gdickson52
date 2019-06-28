from django.shortcuts import render
from core.models import Category, Book
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# My Views

def index(request):
    """View function for home page of site."""

# Count the main objects
    num_books = Book.objects.all().count()
    num_categories = Category.objects.all().count()
    book_list = Book.objects.all()

# Show my added books
    added_books = Book.objects.order_by('date_added') [:3]
    different_categories = Category.objects.all()

    context = {
        'num_books': num_books,
        'num_categories': num_categories,
        'added_books': added_books,
        'different_categories': different_categories,
        'book_list': book_list,
    }

    return render(request, 'index.html', context=context) 

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    model = Book

class CategoriesListView(generic.ListView):
    model = Category

class CategoriesDetailView(generic.DetailView):
    model = Category



