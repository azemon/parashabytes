from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Location, Parasha, Reading, Word

from .tests_util import *


class LocationTest(TestCase):
    def setUp(self):
        self.book = create_book()

    def test_create_location(self):
        location = create_location(book=self.book, chapter=10, verse=11)
        self.assertEqual(location.sortkey, (self.book.sortkey * 10000) + 1000 + 11, 'incorrect start sortkey')

    def test_create_identical_locations_error(self):
        def create_two_locations():
            create_location(self.book)
            create_location(self.book)
        self.assertRaises(IntegrityError, create_two_locations)

    def test_location_text(self):
        book = create_book(english_name='Genesis', hebrew_name='Hebrew Genesis', transliterated_name='Ber', sortkey=2)
        location = create_location(book, chapter=1, verse=1)
        text = location.text()
        english = text['text']
        hebrew = text['he']
        self.assertRegex(english, 'When God began to create')
