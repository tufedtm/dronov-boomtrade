# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Guestbook(models.Model):
    user = models.CharField('Пользователь', max_length=50)
    posted = models.DateTimeField('Опубликовано', auto_now_add=True, db_index=True)
    content = models.TextField('Содержание')

    def __unicode__(self):
        return self.user

    class Meta:
        ordering = ['-posted']
        verbose_name = 'запись гостевой книги'
        verbose_name_plural = 'записи гостевой книги'
