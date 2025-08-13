
from urllib import request

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

    # Filtering, Ordering, Search
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = BookFilter
    ordering_fields = '__all__'
    ordering = ['id']
    search_fields = ['title', 'authors__first_name', 'authors__last_name', 'categories__category']


    # Book availability
    @action(detail=True, methods=['get'], url_path='availability')
    def availability(self, request, pk=None):
        book = self.get_object()
        return Response({
            'title': book.title,
            'available_copies': book.available_copies,
            'total_copies': book.total_copies
        })

    # Borrow book
    @action(detail=False, methods=['post'], url_path='borrow')
    def borrow_book(self, request):
        try:
            book_id = request.data.get('book')
            member_id = request.data.get('member')
            borrow_date = request.data.get('borrow_date')
            due_date = request.data.get('due_date')

            book = Book.objects.get(pk=book_id)
            member = Member.objects.get(pk=member_id)

            if book.available_copies < 1:
                return Response({'error': 'No copies available.'}, status=400)

            Borrowing.objects.create(
                member=member,
                book=book,
                borrow_date=borrow_date,
                due_date=due_date,
                late_fee=0
            )

            book.available_copies -= 1
            book.save()

            return Response({'status': 'Book borrowed successfully.'}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

    # Return book
    @action(detail=False, methods=['post'], url_path='return')
    def return_book(self, request):
        try:
            borrowing_id = request.data.get('borrowing_id')
            borrowing = Borrowing.objects.get(pk=borrowing_id)

            if borrowing.return_date:
                return Response({'error': 'Book already returned.'}, status=400)

            borrowing.return_date = timezone.now().date()

            if borrowing.return_date > borrowing.due_date:
                days_late = (borrowing.return_date - borrowing.due_date).days
                borrowing.late_fee = days_late * 5
            else:
                borrowing.late_fee = 0

            borrowing.save()

            book = borrowing.book
            book.available_copies += 1
            book.save()

            return Response({'status': 'Book returned.', 'late_fee': borrowing.late_fee}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

    @action(detail=False, methods=['get'], url_path='active-borrowings')
    def active_borrowings(self, request):

        member_id = request.query_params.get('member')
        if not member_id:
            return Response({'error': 'member parameter is required.'}, status=400)

        active_borrowings = Borrowing.objects.filter(member_id=member_id, return_date__isnull=True)


        # Serialize the data - you can customize this serializer as needed
        data = []
        for borrow in active_borrowings:
            data.append({
                'borrowing_id': borrow.borrowing_id,
                'book_id': borrow.book.id,
                'book_title': borrow.book.title,
                'borrow_date': borrow.borrow_date,
                'due_date': borrow.due_date,
            })

        return Response(data, status=200)

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
    ordering = ['category_id']  # default ordering

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = MemberFilter

    ordering_fields =  '__all__' # all fields allowed for sorting
    ordering = ['member']  # default ordering

    @action(detail=True, methods=['get'], url_path='borrowings')
    def borrowings(self, request, pk=None):
        member = self.get_object()
        qs = Borrowing.objects.filter(member=member)
        serializer = BorrowingSerializer(qs, many=True)
        return Response(serializer.data)

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

class StatisticsView(APIView):
    def get(self, request):
        total_books = Book.objects.count()
        total_members = Member.objects.count()
        total_borrowings = Borrowing.objects.count()
        active_borrowings = Borrowing.objects.filter(return_date__isnull=True).count()

        return Response({
            'total_books': total_books,
            'total_members': total_members,
            'total_borrowings': total_borrowings,
            'active_borrowings': active_borrowings
        })

class MemberBorrowingHistoryView(APIView):
    serializer_class = BorrowingSerializer

    def get_queryset(self):
        member_id = self.kwargs.get('member_id')
        return Borrowing.objects.filter(member_id=member_id)

    def get(self, request, member_id):
        borrowings = Borrowing.objects.filter(member_id=member_id)
        serializer = BorrowingSerializer(borrowings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

