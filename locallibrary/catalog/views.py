from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    # Count books where title contains "war" (case-insensitive)
    num_books_with_war = Book.objects.filter(title__icontains='war').count()

    # Count genres where name contains "fiction" (case-insensitive)
    num_genres_with_fiction = Genre.objects.filter(name__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits, 
        'num_books_with_war': num_books_with_war,
        'num_genres_with_fiction': num_genres_with_fiction,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book


from .models import Author
from django.views import generic

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'  # optional but more explicit
    template_name = 'catalog/author_list.html'  # must match what you create

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'  # must match what you create


