from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from feeds import RssGoodsListFeed
from views import GoodListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', GoodListView.as_view(), name='goods_index'),
    url(r'^(?P<pk>\d+)/detail/$', GoodDetailView.as_view(), name='goods_detail'),
    url(r'^(?P<pk>\d+)/add/$', permission_required('goods.add_good')(GoodCreate.as_view()), name='goods_create'),
    url(r'^(?P<pk>\d+)/update/$', permission_required('goods.change_good')(GoodUpdate.as_view()), name='goods_update'),
    url(r'^(?P<pk>\d+)/delete/$', permission_required('goods.delete_good')(GoodDelete.as_view()), name='goods_delete'),
    url(r'^(?P<pk>\d+)/feed/rss/$', RssGoodsListFeed(), name='goods_feed_rss'),
]
