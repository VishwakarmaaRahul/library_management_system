from urllib import request

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import viewsets
from .pagination import CustomPagination


from .models import *
from .serializers import (
    LibrarySerializer, BookSerializer, AuthorSerializer, CategorySerializer,
    MemberSerializer, BorrowingSerializer, ReviewSerializer, BookAuthorSerializer,
    BookCategorySerializer
)

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = LibraryFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['library_name']  # default ordering

    # pagination_class = CustomPagination

    # Optional: Custom book detail endpoint inside ViewSet
    @action(detail=True, methods=['get'], url_path='book-detail/(?P<book_id>[^/.]+)')
    def book_detail(self, request, pk=None, book_id=None):
        book = get_object_or_404(Book, id=book_id)
        avg_rating = book.average_rating()
        return Response({
            'book_title': book.title,
            'average_rating': avg_rating
        })


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = BookFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['id']  # default ordering

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = AuthorFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['author_id']  # default ordering

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = CategoryFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['category']  # default ordering

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = MemberFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['member']  # default ordering

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = BorrowingFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['borrowing_id']  # default ordering

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = ReviewFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['review_id']  # default ordering

class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
