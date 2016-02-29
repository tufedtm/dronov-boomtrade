# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=100, unique_for_date='posted')
    description = models.TextField('Краткое описание')
    content = models.TextField('Полное описание')
    posted = models.DateTimeField('Опубликована', default=datetime.now, db_index=True)
    is_commentable = models.BooleanField('Разрешены комментарии', default=True)
    user = models.ForeignKey(User, editable=False)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-posted']
        verbose_name = 'статья блога'
        verbose_name_plural = 'статьи блога'
