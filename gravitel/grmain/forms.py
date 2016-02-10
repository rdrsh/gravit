# -*- coding: utf-8 -*- 

from django import forms
# from django.forms.extras import widgets
# from django.forms.extras.widgets import Textarea

from models import getSubjectChoices

CAPTCHA = '"'

class GravitelForm(forms.Form):
    c = forms.CharField(required=False, initial=CAPTCHA, widget=forms.HiddenInput())
    
    def clean_c(self):
        c = self.cleaned_data.get('c', '')
        if c != CAPTCHA:
            raise forms.ValidationError("Защита от ботов")
        return c
    
    def as_p_br(self):
        s = self.as_p()
        return s.replace('</label> ', '</label><br/>')

class QuestionForm(GravitelForm):
    name = forms.CharField(label=u'Ваше имя')
    email = forms.EmailField(label=u'Ваш e-mail')
    subject = forms.ChoiceField(choices=getSubjectChoices(), label=u'Тема письма')
    text = forms.CharField(label=u'Текст письма', widget=forms.Textarea())

class OrderForm(GravitelForm):
    phone = forms.CharField(label=u'Ваш телефон')
    name = forms.CharField(label=u'Ваше имя')
    ext = forms.CharField(label=u'Дополнительная информация', widget=forms.Textarea())

class LoginForm(GravitelForm):
    login = forms.CharField(label=u'Ваш логин')
    password = forms.CharField(label=u'Ваш пароль', widget=forms.PasswordInput())
