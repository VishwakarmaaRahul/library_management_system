from django.urls import path
from . import views


urlpatterns = [
    path('books/',views.books , name = 'books'),
    path('libraries/',views.libraries,name = 'library'),
    # path('',views.members),
]
# Create your views here.

