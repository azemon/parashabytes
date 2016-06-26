from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Location, Parasha, Reading, Word

from .tests_util import *


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

    def test_create_identical_parashot_error(self):
        def create_parashot():
            Parasha.objects.create(
                hebrew_name='hebrew name',
                transliterated_name='transliterated name',
                notes='parasha note'
            )
            Parasha.objects.create(
                hebrew_name='hebrew name',
                transliterated_name='transliterated name',
                notes='parasha note'
            )
        self.assertRaises(IntegrityError, create_parashot)
