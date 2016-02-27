# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=30, db_index=True, unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', default=0, db_index=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __unicode__(self):
        return self.name
