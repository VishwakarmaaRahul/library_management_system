# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Member)
admin.site.register(Borrowing)
admin.site.register(Review)

