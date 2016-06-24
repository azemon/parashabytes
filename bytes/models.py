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
    hebrew_name = models.CharField(max_length=40, unique=True)
    transliterated_name = models.CharField(max_length=40, unique=True)
    notes = models.CharField(max_length=2000, blank=True)

    class Meta:
        ordering = ['transliterated_name']

    def __str__(self):
        return self.transliterated_name


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
    start_sortkey = models.PositiveIntegerField()  # 10101
    end_sortkey = models.PositiveIntegerField()  # 10209
    description = models.CharField(max_length=40)  # Genesis 1:1-2:9

    class Meta:
        ordering = ['start_sortkey']

    def save(self, *args, **kwargs):
        self.start_sortkey = (self.book.sortkey * 10000) + (self.start_chapter * 100) + self.start_verse
        self.end_sortkey = (self.book.sortkey * 10000) + (self.end_chapter * 100) + self.end_verse
        self.description = '{book} {sc}:{sv}-{ec}:{ev}'.format(book=self.book,
                                                               sc=self.start_chapter, sv=self.start_verse,
                                                               ec=self.end_chapter, ev=self.end_verse)
        super().save(*args, **kwargs)

    def words(self):
        """
        returns a queryset of the set of words within the bounds of this portion
        :return:
        """
        return Word.objects.filter(sortkey__gte=self.start_sortkey).filter(sortkey__lte=self.end_sortkey)

    def __str__(self):
        return self.description


class Word(models.Model):
    """
    one word or phrase mentioned in the Tenach
    """
    english_word = models.CharField(max_length=100, unique=True)
    hebrew_word = models.CharField(max_length=100, unique=True)
    transliterated_word = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.PositiveSmallIntegerField()
    verse = models.PositiveSmallIntegerField()
    sortkey = models.PositiveIntegerField()

    class Meta:
        ordering = ['english_word']

    def save(self, *args, **kwargs):
        self.sortkey = (self.book.sortkey * 10000) + (self.chapter * 100) + self.verse
        super().save(*args, **kwargs)

    def __str__(self):
        return '{english} ({transliterated})'.format(english=self.english_word, transliterated=self.transliterated_word)
