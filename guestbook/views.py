# coding=utf-8
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.dates import ArchiveIndexView
from generic.mixins import CategoryListMixin
from forms import GuestbookForm
from models import Guestbook


class GuestbookView(ArchiveIndexView, CategoryListMixin):
    model = Guestbook
    date_field = 'posted'
    template_name = 'guestbook.html'
    paginate_by = 5
    allow_empty = True
    form = None

    def get(self, request, *args, **kwargs):
        self.form = GuestbookForm()
        return super(GuestbookView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuestbookView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = GuestbookForm(request.POST)

        if self.form.is_valid():
            if self.form.cleaned_data['honeypot'] == '':
                self.form.save()
                messages.add_message(request, messages.SUCCESS, 'Запись успешно добавлена')

                return redirect('guestbook')
        else:

            return super(GuestbookView, self).get(request, *args, **kwargs)
