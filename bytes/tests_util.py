from .models import Book, Location, Parasha, Reading, Word

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


def create_parasha(hebrew_name='hebrew name', transliterated_name='transliterated name', notes='parasha note'):
    parasha = Parasha.objects.create(
        hebrew_name=hebrew_name,
        transliterated_name=transliterated_name,
        notes=notes
    )
    return parasha


def create_reading(book, start_chapter=10, start_verse=11, end_chapter=20, end_verse=22):
    reading = Reading.objects.create(
        book=book,
        start_chapter=start_chapter,
        start_verse=start_verse,
        end_chapter=end_chapter,
        end_verse=end_verse
    )
    return reading


def create_word(english_word='english word', hebrew_word='hebrew word', transliterated_word='transliterated word',
                description='word description'):
    word = Word.objects.create(
        english_word=english_word,
        hebrew_word=hebrew_word,
        transliterated_word=transliterated_word,
        description=description
    )
    return word
