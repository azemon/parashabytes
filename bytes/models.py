from django.db import models

class Parasha(models.Model):
    """
    One parasha, including one or more sections of the Torah and one or more sections of
    the prophets and other writings (haftarah)
    """
    english_name = models.CharField(max_length=40)
    hebrew_name = models.CharField(max_length=40)
    notes = models.CharField(max_length=1000)


class Torah_Portion(models.Model):
    """
    Torah portion including starting and ending book + chapter + verse
    Part of a parasha
    Sort keys are strings in this form:
      BCCVV
      B = book (a, b, c, d, e)
      CC = chapter (00-99)
      VV = verse (00-99)
    """
    BOOKS = (
        ('a', 'Genesis'),
        ('b', 'Exodus'),
        ('c', 'Leviticus'),
        ('d', 'Numbers'),
        ('e', 'Deuteronomy'),
    )
    book = models.CharField(max_length=1, choices=BOOKS)
    start_chapter = models.PositiveSmallIntegerField()
    start_verse = models.PositiveSmallIntegerField()
    end_chapter = models.PositiveSmallIntegerField()
    end_verse = models.PositiveSmallIntegerField()
    parasha = models.ManyToManyField(Parasha)
    # calculated values
    start_sortkey = models.CharField(max_length=5)
    end_sortkey = models.CharField(max_length=5)
    description = models.CharField(max_length=40)


class Word(models.Model):
    """
    one word/food/whatever mentioned in the Tenach
    """
    english_word = models.CharField(max_length=100)
    hebrew_word = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    parasha = models.ManyToManyField(Parasha)
