from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    context = {
        'books': books_query
    }
    return render(request, template, context)


def books_by_date(request, date):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    dates = []
    data = Book.objects.values()
    for b in data:
        dates.append(str(b['pub_date']))
    dates.sort()
    if date:
        books = Book.objects.filter(pub_date=date)
        if date == dates[0]:
            date1 = None
            date2 = dates[1]
        elif date == dates[len(dates) - 1]:
            date1 = dates[dates.index(date) - 1]
            date2 = None
        else:
            date1 = dates[dates.index(date) - 1]
            date2 = dates[dates.index(date) + 1]
    else:
        books = books_query
        date1 = None
        date2 = None
    context = {
        'books': books,
        'previous_page': date1,
        'next_page': date2
    }
    return render(request, template, context)
