# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class ImagePool(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    uploaded = models.DateTimeField('Выгружен', auto_now_add=True, db_index=True)
    image = models.ImageField('Изображение', upload_to='imagepool/%Y/%m')

    class Meta:
        ordering = ['user', '-uploaded']
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __unicode__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.delete(save=False)
        super(ImagePool, self).delete()
