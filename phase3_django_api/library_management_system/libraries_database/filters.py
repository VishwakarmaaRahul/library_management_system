# # libraries/filters.py
# import django_filters
# from .models import Library
# from django.db.models import Q
#
# class LibraryFilter(django_filters.FilterSet):
#     library_name = django_filters.CharFilter(field_name='library_name', lookup_expr='icontains')
#     campus_location = django_filters.CharFilter(method='filter_campus_location')
#     contact_email = django_filters.CharFilter(field_name='contact_email', lookup_expr='exact')
#     phone_number = django_filters.CharFilter(field_name='phone_number', lookup_expr='exact')
#     createdAt = django_filters.DateFromToRangeFilter(field_name='createdAt')
#     updatedAt = django_filters.DateFromToRangeFilter(field_name='updatedAt')
#
#     def filter_campus_location(self, queryset, name, value):
#         return queryset.filter(Q(campus_location__icontains=value) | Q(campus_location__iexact=value))
#
#     class Meta:
#         model = Library
#         fields = ['library_name', 'campus_location', 'contact_email', 'phone_number', 'createdAt', 'updatedAt']
#
#


import django_filters
from .models import Library, Book, Author, Category, Member, Borrowing, Review


class LibraryFilter(django_filters.FilterSet):
    class Meta:
        model = Library
        fields = {
            'library_name': ['icontains'],
            'campus_location': ['icontains'],
            'contact_email': ['icontains'],
            'phone_number': ['exact'],
            'created_at': ['date', 'date__gte', 'date__lte'],
        }


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'isbn': ['exact'],
            'publication_date': ['exact', 'gte', 'lte'],
            'library': ['exact'],
            'available_copies': ['gte', 'lte'],
            'total_copies': ['gte', 'lte'],
        }


class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'birth_date': ['exact', 'gte', 'lte'],
            'nationality': ['icontains'],
        }


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'category': ['icontains'],
            'descriptions': ['icontains'],
        }


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'contact_email': ['icontains'],
            'phone_number': ['icontains'],
            'member_type': ['exact'],
        }


class BorrowingFilter(django_filters.FilterSet):
    class Meta:
        model = Borrowing
        fields = {
            'member': ['exact'],
            'book': ['exact'],
            'borrow_date': ['exact', 'gte', 'lte'],
            'due_date': ['exact', 'gte', 'lte'],
            'return_date': ['exact', 'isnull'],
            'late_fee': ['gte', 'lte'],
        }


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            'member': ['exact'],
            'book': ['exact'],
            'rating': ['exact', 'gte', 'lte'],
            'review_date': ['exact', 'gte', 'lte'],
        }
