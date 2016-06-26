from django.db.utils import IntegrityError
from django.test import TestCase

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


def create_reading(book):
    reading = Reading.objects.create(
        book=book,
        start_chapter=10,
        start_verse=11,
        end_chapter=20,
        end_verse=22,
    )
    return reading


class LocationTest(TestCase):
    def setUp(self):
        self.book = create_book()

    def test_create_location(self):
        location = Location.objects.create(
            book=self.book,
            chapter=10,
            verse=11
        )
        self.assertEqual(location.sortkey, (self.book.sortkey * 10000) + 1000 + 11, 'incorrect start sortkey')

    def test_create_location_error(self):
        def create_two_locations():
            Location.objects.create(
                book=self.book,
                chapter=10,
                verse=11
            )
            Location.objects.create(
                book=self.book,
                chapter=10,
                verse=11
            )
        self.assertRaises(IntegrityError, create_two_locations)


class ParashaTest(TestCase):
    def setUp(self):
        book = create_book()
        self.reading = create_reading(book)

    def test_create_parasha(self):
        parasha = Parasha.objects.create(
            hebrew_name='hebrew name',
            transliterated_name='transliterated name',
            notes='parasha note'
        )
        parasha.reading_set.add(self.reading)
        parasha.save()
        self.assertEqual(parasha.reading_set.first(), self.reading)


class ReadingTest(TestCase):
    def setUp(self):
        self.book = create_book()

    def test_create_reading(self):
        reading = Reading.objects.create(
            book=self.book,
            start_chapter=10,
            start_verse=11,
            end_chapter=20,
            end_verse=22,
        )
        self.assertEqual(reading.start_sortkey, (self.book.sortkey * 10000) + 1000 + 11, 'incorrect start sortkey')
        self.assertEqual(reading.end_sortkey, (self.book.sortkey * 10000) + 2000 + 22, 'incorrect end sortkey')
        self.assertEqual(reading.description, ENGLISH_BOOK + ' 10:11-20:22', 'incorrect description')

    def test_create_two_identical_readings_error(self):
        def create_readings():
            Reading.objects.create(
                book=self.book,
                start_chapter=10,
                start_verse=11,
                end_chapter=20,
                end_verse=22,
            )
            Reading.objects.create(
                book=self.book,
                start_chapter=10,
                start_verse=11,
                end_chapter=20,
                end_verse=22,
            )
        self.assertRaises(IntegrityError, create_readings)


class WordTest(TestCase):
    def setUp(self):
        self.book = create_book()
        self.location = create_location(self.book)

    def test_create_word(self):
        word = Word.objects.create(
            english_word='english',
            hebrew_word='hebrew',
            transliterated_word='transliterate',
            description='the description'
        )
        self.assertIsNotNone(word.pk)

    def test_create_word_with_location(self):
        word = Word.objects.create(
            english_word='english 2',
            hebrew_word='hebrew 2',
            transliterated_word='transliterate 2',
            description='the description'
        )
        word.location.add(self.location)
        retrieved_location = word.location.all().first()
        self.assertEqual(self.location, retrieved_location)

    def test_create_word_with_two_identical_locations(self):
        word = Word.objects.create(
            english_word='english 2',
            hebrew_word='hebrew 2',
            transliterated_word='transliterate 2',
            description='the description'
        )
        word.location.add(self.location)
        word.location.add(self.location)
        self.assertEqual(word.location.all().count(), 1)

    def test_create_word_with_two_different_locations(self):
        word = Word.objects.create(
            english_word='english 2',
            hebrew_word='hebrew 2',
            transliterated_word='transliterate 2',
            description='the description'
        )
        location2 = create_location(self.book, 3, 4)
        word.location.add(self.location)
        word.location.add(location2)
        self.assertEqual(word.location.all().count(), 2)

    def test_create_two_identical_words_error(self):
        def create_two_words():
            Word.objects.create(
                english_word='english',
                hebrew_word='hebrew',
                transliterated_word='transliterate',
                description='the description'
            )
            Word.objects.create(
                english_word='english',
                hebrew_word='hebrew',
                transliterated_word='transliterate',
                description='the description'
            )
        self.assertRaises(IntegrityError, create_two_words)
