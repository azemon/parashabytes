from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Location, Parasha, Reading, Word

from .tests_util import *


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
