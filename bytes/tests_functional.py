from django.test import TestCase

from .tests_util import *

PRINT_A_LOT = False


class FunctionalTest(TestCase):
    def setUp(self):
        self.book1 = create_book(english_name='Book1', hebrew_name='Book1', transliterated_name='Book1', sortkey=1)
        self.book2 = create_book(english_name='book2', hebrew_name='Book2', transliterated_name='book2', sortkey=2)
        
        self.parasha1 = create_parasha('parasha1', transliterated_name='parasha1', notes='parasha1 note')
        self.parasha2 = create_parasha('parasha2', transliterated_name='parasha2', notes='parasha2 note')

        self.reading1 = create_reading(self.book1, start_chapter=1, start_verse=1,
                                       end_chapter=2, end_verse=22)
        self.location1a = create_location(self.book1, chapter=1, verse=5)
        self.location1b = create_location(self.book1, chapter=2, verse=10)

        self.reading2 = create_reading(self.book1, start_chapter=2, start_verse=23,
                                       end_chapter=2, end_verse=39)
        self.location2a = create_location(self.book1, chapter=2, verse=29)
        self.location2b = create_location(self.book1, chapter=2, verse=30)

        self.reading3 = create_reading(self.book2, start_chapter=1, start_verse=1,
                                       end_chapter=7, end_verse=77)
        self.location3a = create_location(self.book2, chapter=3, verse=8)
        self.location3b = create_location(self.book2, chapter=6, verse=16)

        self.reading4 = create_reading(self.book2, start_chapter=40, start_verse=4,
                                       end_chapter=48, end_verse=28)
        self.location4a = create_location(self.book2, chapter=40, verse=5)
        self.location4b = create_location(self.book2, chapter=48, verse=28)

        # word1 is in parasha1 and in reading4 which is outside both parashot
        self.word1 = create_word(english_word='word1', hebrew_word='word1', transliterated_word='word1',
                                 description='word1 description')
        self.word1.location.add(self.location1a, self.location1b, self.location3a, self.location4a)

        # word2 is in both parashot in all three readings
        self.word2 = create_word(english_word='word2', hebrew_word='word2', transliterated_word='word2',
                                 description='description of word2')
        self.word2.location.add(self.location1a, self.location1b, self.location2a, self.location2b,
                                self.location3a, self.location3b)

        # word3 is only in reading4, not in any parashot
        self.word3 = create_word(english_word='word3', hebrew_word='word3', transliterated_word='word3',
                                 description='word3 description')
        self.word3.location.add(self.location4a, self.location4b)

        self.parasha1.reading_set.add(self.reading1, self.reading3)
        self.parasha2.reading_set.add(self.reading2)

        if PRINT_A_LOT:
            print('')
            print('')
            print('parasha1 readings: {}'.format(self.parasha1.reading_set.all()))
            print('parasha1 location_set: {}'.format(self.parasha1.location_set()))
            print('parasha1 word_set: {}'.format(self.parasha1.word_set()))

            print('')
            print('parasha2 readings: {}'.format(self.parasha2.reading_set.all()))
            print('parasha2 location_set: {}'.format(self.parasha2.location_set()))
            print('parasha2 word_set: {}'.format(self.parasha2.word_set()))

    def test_reading_count(self):
        self.assertEqual(self.parasha1.reading_set.all().count(), 2)
        self.assertEqual(self.parasha2.reading_set.all().count(), 1)

    def test_word_location_count(self):
        self.assertEqual(self.word1.location.all().count(), 4)
        self.assertEqual(self.word2.location.all().count(), 6)
        self.assertEqual(self.word3.location.all().count(), 2)

    def test_parasha_words(self):
        self.assertIn(self.word1, self.parasha1.word_set())
        self.assertNotIn(self.word1, self.parasha2.word_set())

        self.assertIn(self.word2, self.parasha1.word_set())
        self.assertIn(self.word2, self.parasha2.word_set())

        self.assertNotIn(self.word3, self.parasha1.word_set())
        self.assertNotIn(self.word3, self.parasha2.word_set())

    def test_parasha_word_locations(self):
        self.word1.parasha(self.parasha1)
        plist = self.word1.sorted_locations_within_parsha()
        should_be = [self.location1a, self.location1b, self.location3a]
        self.assertEqual(plist, should_be)

        self.word2.parasha(self.parasha1)
        plist = self.word2.sorted_locations_within_parsha()
        should_be = [self.location1a, self.location1b, self.location3a, self.location3b]
        self.assertEqual(plist, should_be)

        self.word2.parasha(self.parasha2)
        plist = self.word2.sorted_locations_within_parsha()
        should_be = [self.location2a, self.location2b]
        self.assertEqual(plist, should_be)
