from django.contrib import admin
from .models import Book, Parasha, Reading, Word, Location

admin.site.register(Book)
admin.site.register(Parasha)
admin.site.register(Reading)
admin.site.register(Location)
admin.site.register(Word)
