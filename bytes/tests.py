from django.test import TestCase

from .models import *


ENGLISH_BOOK = 'english book'


def create_book():
    book = Book.objects.create(
        english_name=ENGLISH_BOOK,
        hebrew_name='hebrew book',
        transliterated_name='transliterated book',
        sortkey=1
    )
    return book


def create_portion(book):
    portion = Portion.objects.create(
        book=book,
        start_chapter=10,
        start_verse=11,
        end_chapter=20,
        end_verse=22,
    )
    return portion


class ParashaTest(TestCase):
    def setUp(self):
        book = create_book()
        self.portion = create_portion(book)

    def test_create_parasha(self):
        parasha = Parasha.objects.create(
            english_name='english name',
            hebrew_name='hebrew name',
            transliterated_name='transliterated name',
            notes='parasha note'
        )
        parasha.portion_set.add(self.portion)
        parasha.save()
        self.assertEqual(parasha.portion_set.first(), self.portion)


class PortionTest(TestCase):
    def setUp(self):
        self.book = create_book()

    def test_create_portion(self):
        portion = Portion.objects.create(
            book=self.book,
            start_chapter=10,
            start_verse=11,
            end_chapter=20,
            end_verse=22,
        )
        self.assertEqual(portion.start_sortkey, (self.book.sortkey * 10000) + 1000 + 11, 'incorrect start sortkey')
        self.assertEqual(portion.end_sortkey, (self.book.sortkey * 10000) + 2000 + 22, 'incorrect end sortkey')
        self.assertEqual(portion.description, ENGLISH_BOOK + ' 10:11-20:22', 'incorrect description')


class WordTest(TestCase):
    def setUp(self):
        self.book = create_book()

    def test_create_word(self):
        word = Word.objects.create(
            english_word='english',
            hebrew_word='hebrew',
            transliterated_word='transliterate',
            description='the description',
            book=self.book,
            chapter=2,
            verse=3
        )
        self.assertEqual(word.sortkey, (self.book.sortkey * 10000) + 200 + 3, 'incorrect sortkey')
