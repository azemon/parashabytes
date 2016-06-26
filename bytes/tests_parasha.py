from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Location, Parasha, Reading, Word

from .tests_util import *


class ParashaTest(TestCase):
    def setUp(self):
        book = create_book()
        self.reading = create_reading(book)

    def test_create_parasha(self):
        parasha = create_parasha()
        parasha.reading_set.add(self.reading)
        parasha.save()
        self.assertEqual(parasha.reading_set.first(), self.reading)

    def test_create_identical_parashot_error(self):
        def create_parashot():
            create_parasha()
            create_parasha()
        self.assertRaises(IntegrityError, create_parashot)
