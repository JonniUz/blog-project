from books.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

from .models import Book, Review


class BookListView(ListView):
    context_object_name = 'books'
    model = Book


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
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
    if request.user.is_authenticated:
        if request.method=='POST':
            newReview = Review(book_id=id, user=request.user)
            form = ReviewForm(request.POST, request.FILES, instance=newReview)
            if form.is_valid():
                form.save()
        form = ReviewForm()
    return redirect(f'/book/{id}')

'''
       body = request.POST['body']
       newReview = Review(body=body, book_id=id, user=request.user)

       if len(request.FILES) != 0:
            image = request.FILES['image']
            fs = FileSystemStorage()
            name = fs.save(image.name, image)
            newReview.image = fs.url(name)

       newReview.save()
    return HttpResponseRedirect(reverse('book.all'))
'''


    # fs = FileSystemStorage()
    # name = None
    # if request.user.is_authenticated:
    #     body = request.POST['body']
    #     if len(request.FILES) != 0:
    #         image = request.FILES['image']
    #         fs = FileSystemStorage()
    #         name = fs.save(image.name, image)
    #     Review.objects.update_or_create(body=body, book_id=id, user=request.user, image=fs.url(name))
    # return HttpResponseRedirect(reverse('book.all'))


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    return render(request, 'books/book_list.html', {'books': books})
