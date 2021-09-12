from typing import Generic
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from .models import Book, Review


class BookListView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'
    model = Book

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        return context

def show(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'books/show.html', context)


def review(request, id):
    body = request.POST['review']
    newReview = Review.objects.update_or_create(body=body, book_id=id)
    # return redirect('book.all')
    return HttpResponseRedirect(reverse('book.all'))
