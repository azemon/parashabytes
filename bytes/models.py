from django.db import models

class Book(models.Model):
    """
    One book in the Tanach
    """
    english_name = models.CharField(max_length=20, unique=True)
    hebrew_name = models.CharField(max_length=20, unique=True)
    transliterated_name = models.CharField(max_length=20, unique=True)
    sortkey = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ['sortkey']

    def __str__(self):
        return self.english_name


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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_chapter = models.PositiveSmallIntegerField()
    start_verse = models.PositiveSmallIntegerField()
    end_chapter = models.PositiveSmallIntegerField()
    end_verse = models.PositiveSmallIntegerField()
    parasha = models.ManyToManyField(Parasha)
    # calculated values
    start_sortkey = models.PositiveIntegerField() # 10101
    end_sortkey = models.PositiveIntegerField() # 10209
    description = models.CharField(max_length=40) # Genesis 1:1-2:9


class Word_Location(models.Model):
    """
    location of a word in the Tenach
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.PositiveSmallIntegerField()
    verse = models.PositiveSmallIntegerField()


class Word(models.Model):
    """
    one word or phrase mentioned in the Tenach
    """
    english_word = models.CharField(max_length=100, unique=True)
    hebrew_word = models.CharField(max_length=100, unique=True)
    transliterated_word = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, null=True)
    word_location = models.ManyToManyField(Word_Location)
