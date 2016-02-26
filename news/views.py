# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from generic.mixins import CategoryListMixin, PageNumberMixin
from generic.controllers import PageNumberView
from models import New


class NewsListView(ArchiveIndexView, CategoryListMixin):
    model = New
    date_field = 'posted'
    template_name = 'news_index.html'
    paginate_by = 5
    allow_empty = True
    allow_future = True


class NewDetailView(DetailView, PageNumberMixin):
    model = New
    template_name = 'new.html'


class NewCreate(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = New
    fields = '__all__'
    template_name = 'new_add.html'
    success_url = reverse_lazy('news_index')
    success_message = 'Новость успешно создана'


class NewUpdate(SuccessMessageMixin, PageNumberView, UpdateView, PageNumberMixin):
    model = New
    fields = '__all__'
    template_name = 'new_update.html'
    success_url = reverse_lazy('news_index')
    success_message = 'Новость успешно обновлена'


class NewDelete(PageNumberView, DeleteView, PageNumberMixin):
    model = New
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news_index')

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Новость успешно удалена')

        return super(NewDelete, self).post(request, *args, **kwargs)
