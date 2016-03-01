from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from feeds import RssNewsListFeed, AtomNewsListFeed
from views import NewsListView, NewDetailView, NewCreate, NewUpdate, NewDelete

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_index'),
    url(r'^(?P<pk>\d+)/$', NewDetailView.as_view(), name='news_detail'),
    url(r'^add/$', permission_required('news.add_new')(NewCreate.as_view()), name='news_add'),
    url(r'^(?P<pk>\d+)/update/$', permission_required('news.update_new')(NewUpdate.as_view()), name='news_update'),
    url(r'^(?P<pk>\d+)/delete/$', permission_required('news.delete_new')(NewDelete.as_view()), name='news_delete'),
    url(r'^feed/rss/$', RssNewsListFeed(), name='news_feed_rss'),
    url(r'^feed/atom/$', AtomNewsListFeed(), name='news_feed_atom'),
]
