from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Location, Parasha, Reading, Word

from .tests_util import *


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
