from urllib import request

from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import (
    LibrarySerializer, BookSerializer, AuthorSerializer, CategorySerializer,
    MemberSerializer, BorrowingSerializer, ReviewSerializer, BookAuthorSerializer,
    BookCategorySerializer
)

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def book_detail(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        avg_rating = book.average_rating()

        context = {
            'book': book,
            'average_rating': avg_rating,
        }
        return render(request, 'books/book_detail.html', context)

    def get_queryset(self):
        queryset = Library.objects.all()

        # Handle sorting
        sort_by = self.request.query_params.get('sort_by', 'library_name')
        allowed_sort_fields = [
            'library_id', '-library_id',
            'library_name', '-library_name',
            'campus_location', '-campus_location',
            'created_at', '-created_at',
            'updated_at', '-updated_at',
        ]
        if sort_by in allowed_sort_fields:
            queryset = queryset.order_by(sort_by)

        return queryset


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
