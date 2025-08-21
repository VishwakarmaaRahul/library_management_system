import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from libraries_database.models import Borrowing
from .factories import (
    LibraryFactory, BookFactory, MemberFactory,
    AuthorFactory, CategoryFactory, BorrowingFactory
)


@pytest.fixture
def api_client():
    return APIClient()


# ---------------- LIBRARY ENDPOINTS ----------------
@pytest.mark.django_db
def test_list_libraries(api_client):
    LibraryFactory.create_batch(3)
    url = reverse("library-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_create_library(api_client):
    url = reverse("library-list")
    data = {"name": "Central Library"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Central Library"


# ---------------- BOOK ENDPOINTS ----------------
@pytest.mark.django_db
def test_list_books(api_client):
    BookFactory.create_batch(2)
    url = reverse("book-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_book(api_client):
    library = LibraryFactory()
    url = reverse("book-list")
    data = {
        "title": "Test Driven Development",
        "total_copies": 5,
        "available_copies": 5,
        "library": library.pk,
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["title"] == "Test Driven Development"


# ---------------- AUTHOR ENDPOINTS ----------------
@pytest.mark.django_db
def test_list_authors(api_client):
    AuthorFactory.create_batch(2)
    url = reverse("author-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_author(api_client):
    url = reverse("author-list")
    data = {"name": "George Orwell"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "George Orwell"


# ---------------- CATEGORY ENDPOINTS ----------------
@pytest.mark.django_db
def test_list_categories(api_client):
    CategoryFactory.create_batch(2)
    url = reverse("category-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_category(api_client):
    url = reverse("category-list")
    data = {"name": "Fiction"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Fiction"


# ---------------- MEMBER ENDPOINTS ----------------
@pytest.mark.django_db
def test_list_members(api_client):
    MemberFactory.create_batch(2)
    url = reverse("member-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_member(api_client):
    url = reverse("member-list")
    data = {
        "first_name": "Rahul",
        "last_name": "Vishwakarma",
        "email": "rahul@test.com"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["first_name"] == "Rahul"


# ---------------- BORROWING FLOW ----------------
@pytest.mark.django_db
def test_borrow_and_return_book(api_client):
    book = BookFactory()
    member = MemberFactory()

    # Borrow
    url = reverse("book-borrow")
    borrow_data = {
        "book_id": book.pk,
        "member_id": member.pk,
        "borrow_date": "2025-08-21",
        "due_date": "2025-08-28",
    }
    borrow_response = api_client.post(url, borrow_data, format="json")
    assert borrow_response.status_code == 200
    assert borrow_response.data["status"] == "Book borrowed successfully."

    borrowing = Borrowing.objects.first()

    # Return
    url = reverse("book-return")
    return_response = api_client.post(url, {"borrowing_id": borrowing.pk}, format="json")
    assert return_response.status_code == 200
    assert "Book returned" in return_response.data["status"]


# ---------------- CUSTOM VIEWS ----------------
@pytest.mark.django_db
def test_statistics_view(api_client):
    BookFactory.create_batch(3)
    url = reverse("statistics")
    response = api_client.get(url)
    assert response.status_code == 200
    assert "total_books" in response.data
    assert response.data["total_books"] == 3


@pytest.mark.django_db
def test_member_borrowing_history(api_client):
    borrowing = BorrowingFactory()
    url = reverse("member-borrowing-history", args=[borrowing.member.pk])
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
