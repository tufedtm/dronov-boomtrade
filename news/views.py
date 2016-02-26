from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from generic.mixins import CategoryListMixin, PageNumMixin
from models import New


class NewsListView(ArchiveIndexView, CategoryListMixin):
    model = New
    date_field = 'posted'
    template_name = 'news_index.html'
    paginate_by = 5
    allow_empty = True
    allow_future = True


class NewDetailView(DetailView, PageNumMixin):
    model = New
    template_name = 'new.html'
