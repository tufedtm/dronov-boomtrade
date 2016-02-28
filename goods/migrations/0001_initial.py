# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('content', models.TextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('price', models.FloatField(db_index=True, verbose_name='\u0426\u0435\u043d\u0430, \u0440.')),
                ('price_acc', models.FloatField(blank=True, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0441\u043a\u0438\u0434\u043a\u0438, \u0440.')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='\u0415\u0441\u0442\u044c \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')),
                ('featured', models.BooleanField(db_index=True, default=False, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u044b\u0439')),
                ('image', models.ImageField(upload_to='goods/list', verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goods/detail', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good', verbose_name='\u0422\u043e\u0432\u0430\u0440')),
            ],
            options={
                'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a \u0442\u043e\u0432\u0430\u0440\u0443',
                'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043a \u0442\u043e\u0432\u0430\u0440\u0443',
            },
        ),
    ]
