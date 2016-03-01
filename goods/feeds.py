# coding=utf-8
from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from models import Category


class RssGoodsListFeed(Feed):
    def get_object(self, request, *args, **kwargs):
        try:
            return Category.objects.get(pk=kwargs['pk'])
        except Category.DoesNotExist:
            raise ObjectDoesNotExist('Нет такой категории')

    def title(self, obj):
        return obj.name
