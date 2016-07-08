from django.db import models


BOOKS = {
    'Genesis': 1,
    'Exodus': 2,
    'Leviticus': 3,
    'Numbers': 4,
    'Deuteronomy': 5,
}


def sortkey(book, chapter, verse):
    """
    return the sortkey for a location. they are of the form BBCCVV
    :param book: Book
    :param chapter: integer
    :param verse: integer
    :return: integer
    """
    return (BOOKS[book] * 10000) + (chapter * 100) + verse


class BibleManager(models.Manager):
    def contains_hebrew_word(self, word='דֶּשֶׁא'):
        """
        find all Bible verses containing a Hebrew word.
        We need to use this because the filter(hebrew_word__contains=...) doesn't work right with Hebrew
        :param word:
        :return:
        """
        sql = """select sortkey, book, chapter, verse, hebrew_text
                 from bible_bible
                 where hebrew_text like '%%%s%%' """
        raw_query_set = self.raw(sql, [word])
        result_list = []
        for b in raw_query_set:
            result_list.append(b)
        return result_list



class Bible(models.Model):
    """
    text of the Bible, in Hebrew only for now
    """
    sortkey = models.PositiveIntegerField(primary_key=True)
    book = models.CharField(max_length=20)
    chapter = models.PositiveSmallIntegerField()
    verse = models.PositiveSmallIntegerField()
    hebrew_text = models.CharField(max_length=2000)

    objects = BibleManager()

    def reference(self):
        return '{book} {chapter}:{verse}'.format(book=self.book, chapter=self.chapter, verse=self.verse)

    def save(self, *args, **kwargs):
        self.sortkey = sortkey(self.book, self.chapter, self.verse)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference()
