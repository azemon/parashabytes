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
