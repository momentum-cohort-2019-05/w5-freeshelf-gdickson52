from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter a book category (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=200, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    category = models.ManyToManyField(Category, help_text='Select a category for this book')
    
    url = models.URLField(max_length=200)
    
    date_added = models.DateTimeField(auto_now_add=True)

    favorited = models.ManyToManyField(User, through='favorite')




    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])        

class Favorite(models.Model):
    """A user can select their favorite books"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_selected = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-user_selected']
    
    def __str__(self):
        """String to represent the object that is favorited."""
        return f"{self.user.username} - {self.book.title}"


    


