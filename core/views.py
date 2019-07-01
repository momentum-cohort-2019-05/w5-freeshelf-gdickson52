from django.shortcuts import render
from core.models import Category, Book, Favorite
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


# My Views

def index(request):
    """View function for my home page."""


    num_books = Book.objects.all().count()
    num_categories = Category.objects.all().count()
    book_list = Book.objects.all()


    added_books = Book.objects.order_by('date_added') [:3]
    categories = Category.objects.all()

    context = {
        'num_books': num_books,
        'num_categories': num_categories,
        'added_books': added_books,
        'categories': categories,
        'book_list': book_list,
    }

    return render(request, 'index.html', context=context) 

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    model = Book

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category


@login_required
def favorites(request):
    """A function that shows the books that have been favorited by a user."""
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'core/user_favorites.html', {'favorites': favorites})

@login_required
def choose_favorites(request,pk):
    """This function allows user to favorite a book or unfavorite a book."""

