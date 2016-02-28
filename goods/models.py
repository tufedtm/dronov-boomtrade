# coding=utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from categories.models import Category


class Good(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория')
    description = models.TextField('Краткое описание')
    content = models.TextField('Полное описание')
    price = models.FloatField('Цена, р.', db_index=True)
    price_acc = models.FloatField('Цена с учетом скидки, р.', null=True, blank=True)
    in_stock = models.BooleanField('Есть в наличии', default=True, db_index=True)
    featured = models.BooleanField('Рекомендуемый', default=False, db_index=True)
    image = models.ImageField('Основное изображение', upload_to='goods/list')

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        try:
            this_record = Good.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(Good, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False, *args, **kwargs):
        self.image.delete(save=False)
        super(Good, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class GoodImage(models.Model):
    good = models.ForeignKey(Good, verbose_name='Товар')
    image = models.ImageField('Дополнительное изображение', upload_to='goods/detail')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        try:
            this_record = GoodImage.objects.get(pk=self.pk)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(GoodImage, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False, *args, **kwargs):
        self.image.delete(save=False)
        super(GoodImage, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'изображение к товару'
        verbose_name_plural = 'изображения к товару'
