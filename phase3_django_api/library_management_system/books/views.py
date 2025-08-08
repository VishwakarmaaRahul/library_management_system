from django.http import HttpResponse

def books(request):
    book = [
        {'book_id' : 1 , 'title' : 'Introduction to Algorithms', 'isbn' : '9780262033848' }
    ]
    return HttpResponse(book)

def libraries(request):
    library =[{'library_id' : 102, 'library_name': 'Central Library', 'campus_location' :'Main Campus'}]
    return HttpResponse(library)