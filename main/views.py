from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import ClassListMixin


class MainPageView(TemplateView, ClassListMixin):
    template_name = 'mainpage.html'
