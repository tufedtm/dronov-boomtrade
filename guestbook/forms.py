# coding=utf-8
from django import forms
from guestbook.models import Guestbook


class GuestbookForm(forms.ModelForm):

    class Meta:
        model = Guestbook
        fields = '__all__'

    user = forms.CharField(label='Пользователь', max_length=50)
    content = forms.CharField(label='Содержание', widget=forms.Textarea)
    honeypot = forms.CharField(required=False)
