from .models import Book, Location, Reading


ENGLISH_BOOK = 'english book'


def create_book(english_name=ENGLISH_BOOK, hebrew_name='hebrew book', transliterated_name='transliterated book',
                sortkey=1):
    book = Book.objects.create(
        english_name=english_name,
        hebrew_name=hebrew_name,
        transliterated_name=transliterated_name,
        sortkey=sortkey
    )
    return book


def create_location(book, chapter=1, verse=1):
    location = Location.objects.create(
        book=book,
        chapter=chapter,
        verse=verse
    )
    return location


def create_reading(book):
    reading = Reading.objects.create(
        book=book,
        start_chapter=10,
        start_verse=11,
        end_chapter=20,
        end_verse=22,
    )
    return reading
