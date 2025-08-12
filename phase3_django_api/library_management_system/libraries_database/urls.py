from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'libraries',LibraryViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'members',MemberViewSet)
router.register(r'borrowings',BorrowingViewSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'bookauthors', BookAuthorViewSet)
router.register(r'bookcategories', BookCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
 path('api/members/<int:member_id>/borrowings/', MemberBorrowingHistoryView.as_view(), name='member-borrowings'),
    path('statistics/', StatisticsView.as_view(), name='library-statistics'),

]
