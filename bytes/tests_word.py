from django.db.utils import IntegrityError
from django.test import TestCase

from .tests_util import *


class WordTest(TestCase):
    def setUp(self):
        self.book = create_book()
        self.location = create_location(self.book)

    def test_create_word(self):
        word = create_word()
        self.assertIsNotNone(word.pk)
        self.assertIsNotNone(word.slug)

    def test_create_word_with_location(self):
        word = create_word()
        word.location.add(self.location)
        retrieved_location = word.location.all().first()
        self.assertEqual(self.location, retrieved_location)

    def test_create_word_with_two_identical_locations(self):
        word = create_word()
        word.location.add(self.location)
        word.location.add(self.location)
        self.assertEqual(word.location.all().count(), 1)

    def test_create_word_with_two_different_locations(self):
        word = create_word()
        word.location.add(self.location)
        location2 = create_location(self.book, 3, 4)
        word.location.add(location2)
        self.assertEqual(word.location.all().count(), 2)

    def test_create_two_identical_words_error(self):
        def create_two_words():
            create_word()
            create_word()
        self.assertRaises(IntegrityError, create_two_words)

    def test_word_str(self):
        word = create_word(
            english_word='english test',
            hebrew_word='hebrew test',
            transliterated_word='transliterated',
            description='nothing to say here',
        )
        self.assertEqual(str(word), 'english test (transliterated)')
