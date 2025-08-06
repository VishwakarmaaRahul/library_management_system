from django.http import HttpResponse

def books(request):
    book = [
        {'book_id' : 1 , 'title' : 'Introduction to Algorithms', 'isbn' : '9780262033848' }
    ]
    return HttpResponse(book)