from django.db import models

class Parasha(models.Model):
    """
    One parasha, including one or more sections of the Tanach
    """
    english_name = models.CharField(max_length=40, unique=True)
    hebrew_name = models.CharField(max_length=40, unique=True)
    transliterated_name = models.CharField(max_length=40, unique=True)
    notes = models.CharField(max_length=2000, null=True)


class Portion(models.Model):
    """
    Portion of the Tanach including starting and ending book + chapter + verse
    Part of one or more parashot
    Sort keys are integers in this form:
      BCCVV
      B = book (1, 2, ...)
      CC = chapter (00-99)
      VV = verse (00-99)
    """
    start_chapter = models.PositiveSmallIntegerField()
    start_verse = models.PositiveSmallIntegerField()
    end_chapter = models.PositiveSmallIntegerField()
    end_verse = models.PositiveSmallIntegerField()
    parasha = models.ManyToManyField(Parasha)
    # calculated values
    start_sortkey = models.PositiveIntegerField() # 10101
    end_sortkey = models.PositiveIntegerField() # 10209
    description = models.CharField(max_length=40) # Genesis 1:1-2:9


class Book(models.Model):
    """
    One book in the Tanach
    """
    english_name = models.CharField(max_length=20, unique=True)
    hebrew_name = models.CharField(max_length=20, unique=True)
    transliterated_name = models.CharField(max_length=20, unique=True)
    sort_key = models.PositiveSmallIntegerField(unique=True)
    portion = models.ForeignKey(Portion, on_delete=models.CASCADE)


class Word(models.Model):
    """
    one word/food/whatever mentioned in the Tenach
    """
    english_word = models.CharField(max_length=100, unique=True)
    hebrew_word = models.CharField(max_length=100, unique=True)
    transliterated_word = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, null=True)
    parasha = models.ManyToManyField(Parasha)
