# coding=utf-8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.feedgenerator import Atom1Feed
from models import New


class RssNewsListFeed(Feed):
    title = 'Новости сайта "Веник-Торг"'
    description = title
    link = reverse_lazy('news_index')

    def items(self):
        return New.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.posted

    def item_link(self, item):
        return reverse('news_detail', args=[item.pk])


class AtomNewsListFeed(RssNewsListFeed):
    feed_type = Atom1Feed
    subtitle = RssNewsListFeed.description
