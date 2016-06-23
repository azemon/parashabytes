from django.contrib import admin
from .models import Book, Parasha, Portion, Word_Location, Word


admin.site.register(Book)
admin.site.register(Parasha)
admin.site.register(Portion)
admin.site.register(Word_Location)
admin.site.register(Word)
