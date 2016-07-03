import json

from django.test import TestCase

from .views import TextRetrieveView, NormalizeLocationView


class NormalizeLocationViewTest(TestCase):
    def test_valid_location(self):
        response = NormalizeLocationView(None, 'ex 2.12')
        data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(data['book']['english'], 'Exodus')
        self.assertEqual(data['chapter'], 2)
        self.assertEqual(data['verse'], 12)

    def test_invalid_book(self):
        response = NormalizeLocationView(None, 'xyzzy 1:1')
        data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(data['error'], 'invalid location')

    def test_invalid_chapter(self):
        response = NormalizeLocationView(None, 'deut 99:1')
        data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(data['error'], 'invalid location')

    def test_invalid_verse(self):
        response = NormalizeLocationView(None, 'deut 1:99')
        data = json.loads(str(response.content, encoding='utf-8'))
        self.assertEqual(data['error'], 'invalid location')


class RetrieveViewTest(TestCase):
    def test_location_text(self):
        response = TextRetrieveView(None, 'Genesis 1:1')
        text = str(response.content, encoding='utf-8')
        self.assertRegex(text, 'When God began to create')
