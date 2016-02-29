# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class New(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique_for_date='posted')
    description = models.TextField('Краткое содержание')
    content = models.TextField('Полное содержание')
    posted = models.DateTimeField('Опибликована', default=datetime.now)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-posted']
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
