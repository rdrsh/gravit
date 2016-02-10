# -*- coding: utf-8 -*- 

from types import *

from django.db import models

####################################################################################################
## trim
####################################################################################################

def trm(s, l, postfix='...'):
    if len(s) <= l:
        return s
    else:
        return s[:l]+postfix

####################################################################################################
## banners
####################################################################################################

class Banner(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    content = models.TextField(verbose_name=u'Текст')
    bg = models.ImageField(upload_to='img/banner/', verbose_name=u'Изображение')

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('sort_no',)
        verbose_name = u"Баннер"
        verbose_name_plural = u"Баннеры"

w = 172
h = 146
class Banner2(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    img = models.ImageField(upload_to='img/banner2/', verbose_name=u'Изображение (%d X %d)' % (w, h))

    def __unicode__(self):
        return self.url
    
    class Meta:
        ordering = ('sort_no',)
        verbose_name = u"Баннер №2"
        verbose_name_plural = u"Баннеры №2"

####################################################################################################
## menu
####################################################################################################

class MenuModel(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        abstract = True

class MenuTop(MenuModel):
    class Meta():
        verbose_name = u"Пункт верхнего меню"
        verbose_name_plural = u"Верхнее меню"
        ordering = ('sort_no',)

class MenuBottom(MenuModel):
    class Meta:
        verbose_name = u"Пункт нижнего меню"
        verbose_name_plural = u"Нижнее меню"
        ordering = ('sort_no',)

class MenuStart(MenuModel):
    class Meta:
        verbose_name = u'Пункт меню "С чего начать"'
        verbose_name_plural = u'Меню "С чего начать"'
        ordering = ('sort_no',)

####################################################################################################
## about
####################################################################################################

class Page(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Содержание', blank=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Страницу"
        verbose_name_plural = u"Страницы"
        ordering = ('sort_no',)
        
class News(models.Model):
    created = models.DateField(auto_now=True, verbose_name=u'Дата')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    content = models.TextField(verbose_name=u'Текст')

    def __unicode__(self):
        return "%s. %s" % (self.created, self.title)
        
    class Meta:
        verbose_name = u"новость"
        verbose_name_plural = u"Новости"
        ordering = ('-created',)
        
w = 75
h = 75
class Employee(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Описание')
    img = models.ImageField(upload_to='img/employee/', verbose_name=u'Изображение (%d X %d)' % (w, h))

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Сотрудника"
        verbose_name_plural = u"Сотрудники"
        ordering = ('sort_no',)

w = 60
h = 80
class Certificate(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Содержание')
    img = models.ImageField(upload_to='img/certificate/', verbose_name=u'Изображение (thumnail смасштабирется до %d X %d)' % (w, h))

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Сертификат"
        verbose_name_plural = u"Сертификаты"
        ordering = ('sort_no',)

def prefixHttp(url):
    if url.lower().split('://')[0] not in ('http', 'https'):
        url = 'http://'+url
    return url

w = 75
h = 75
class Partner(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Описание')
    extr_url = models.CharField(max_length=255, verbose_name=u'Ссылка', unique=True)
    img = models.ImageField(upload_to='img/partner/', verbose_name=u'Изображение (%d X %d)' % (w, h))
    
    def extr_url_http(self):
        return prefixHttp(self.extr_url)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Партнера"
        verbose_name_plural = u"Партнеры"
        ordering = ('sort_no',)

w = 75
h = 75
class Client(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Описание')
    extr_url = models.CharField(max_length=255, verbose_name=u'Ссылка', unique=True)
    img = models.ImageField(upload_to='img/partner/', verbose_name=u'Изображение (%d X %d)' % (w, h))

    def extr_url_http(self):
        return prefixHttp(self.extr_url)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Клиента"
        verbose_name_plural = u"Клиенты"
        ordering = ('sort_no',)

####################################################################################################
## 
####################################################################################################

class HelpCat(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Категория')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Категорию помощи"
        verbose_name_plural = u"Категории помощи"
        ordering = ('sort_no',)
        
class HelpSubcat(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    cat = models.ForeignKey(HelpCat, verbose_name=u'Категория')
    title = models.CharField(max_length=255, verbose_name=u'Подкатегория')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)

    def __unicode__(self):
        return '%s/%s' % (self.cat.title, self.title)
    
    class Meta:
        verbose_name = u"Подкатегорию помощи"
        verbose_name_plural = u"Подкатегории помощи"
        ordering = ('sort_no',)
        
class Help(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    subcat = models.ForeignKey(HelpSubcat, verbose_name=u'Категория')
    question = models.TextField(verbose_name=u'Вопрос')
    answer = models.TextField(verbose_name=u'Ответ')
    created = models.DateTimeField(auto_now=True, verbose_name=u'Дата')

    def __unicode__(self):
        return trm(self.question, 32)
    
    class Meta:
        verbose_name = u"Помощь"
        verbose_name_plural = u"Помощь"
        ordering = ('sort_no',)

class Vendor(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название')

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Производителя"
        verbose_name_plural = u"Производители"

class ProductCat(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Категорию продукта"
        verbose_name_plural = u"Категории продукта"
        ordering = ('sort_no',)

wSm = 70
hSm = 70
w = 160
h = 160
class Product(models.Model):
    wSm = wSm
    hSm = hSm
    w = w
    h = h
    cat = models.ForeignKey(ProductCat, verbose_name=u'Категория')
    vendor = models.ForeignKey(Vendor, verbose_name=u'Производитель')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    annotation = models.TextField(verbose_name=u'Анотация')
    description = models.TextField(verbose_name=u'Описание')
    price = models.PositiveIntegerField(verbose_name=u'Цена')
    img = models.ImageField(upload_to='img/product/', verbose_name=u'Изображение (%d X %d)' % (w, h))

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"
        ordering = ('-price',)

class Service(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    title = models.CharField(max_length=255, verbose_name=u'Название')
    content = models.TextField(verbose_name=u'Содержание')
    settings = models.TextField(verbose_name=u'Как настроить', blank=True)
    video = models.TextField(verbose_name=u'Видео', null=True, blank=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Сервис"
        verbose_name_plural = u"Сервисы"
        ordering = ('sort_no',)

w = 80
h = 80
class Payment(models.Model):
    w = w
    h = h
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    title = models.CharField(max_length=255, verbose_name=u'Название')
    annotation = models.TextField(verbose_name=u'Аннотация')
    content = models.TextField(verbose_name=u'Содержание')
    img = models.ImageField(upload_to='img/payment/', verbose_name=u'Изображение (%d X %d)' % (w, h))

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Оплату"
        verbose_name_plural = u"Оплаты"
        ordering = ('sort_no',)

####################################################################################################
## phone
####################################################################################################

class NumberType(models.Model):
    sort_no = models.FloatField(verbose_name=u'Порядковый номер')
    title = models.CharField(max_length=255, verbose_name=u'Название', unique=True)
    url = models.CharField(max_length=255, verbose_name=u'URL', unique=True)
    price = models.IntegerField(verbose_name=u'Цена')

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Тип номера телефона"
        verbose_name_plural = u"Типы номеров телефонов"
        ordering = ('sort_no',)

class Number(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Номер', unique=True)
    type = models.ForeignKey(NumberType, verbose_name=u'Тип')

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Номер телефона"
        verbose_name_plural = u"Номера телефонов"
        
class CallModel(models.Model):
    code = models.IntegerField(verbose_name=u'Код', unique=True)
    direction = models.CharField(max_length=255, verbose_name=u'Направление', unique=True)
    price = models.FloatField(verbose_name=u'Цена')
    price_mob = models.FloatField(verbose_name=u'Цена на мобильный')

    def __unicode__(self):
        return self.direction

class CallRussia(CallModel):
    class Meta:
        verbose_name = u"Звонок (рус)"
        verbose_name_plural = u"Звонки (рус)"

class CallSng(CallModel):
    class Meta:
        verbose_name = u"Звонок (СНГ)"
        verbose_name_plural = u"Звонки (СНГ)"

class CallForeign(CallModel):
    class Meta:
        verbose_name = u"Звонок (загр)"
        verbose_name_plural = u"Звонки (загр)"

####################################################################################################
## VARS
####################################################################################################

class Settings(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название', unique=True)
    value = models.CharField(max_length=255, verbose_name=u'Значение')
    comment = models.CharField(max_length=255, verbose_name=u'Коментарий')
    
    def __unicode__(self):
        return u'%s = %s' % (self.comment, self.value)
        
    class Meta:
        verbose_name = u"Переменная"
        verbose_name_plural = u"Переменные"
        ordering = ('name',)

defaultVars = {
    'perPageNews': 10,
    'perPageHelp': 10,
    'perPageProduct': 1,
    
    'pricePerson': 100000,
    'priceFax': 200000,
    'priceEmail': 300000,
    'priceLine': 1000,

    'contactIcq': '456 56 56, 198 34 34',
    'contactSkype': 'gravitel',
    'contactPhone': '+7 (495) 740 06 50',
    'contactEmail': 'info@gravitel.ru',
    'contactEmailQuestion': 'info@gravitel.ru',
    'contactEmailOrder': 'info@gravitel.ru',
}

def getSubjectChoices():
    return [('__error__', u'Сообщение об ошибке'), ('__fichure_request__', u'Пожелание')] + [(i.url, i.title) for i in HelpCat.objects.all()]
    
    
def updateDict(d, d2):
    result = {}
    for k, v in d2.items():
        result[k] = d.get(k, v)
    return result
    
def getVars():
    vars = dict([i.name, i.value] for i in Settings.objects.all())
    vars = updateDict(vars, defaultVars)
    for k, v2 in defaultVars.items():
        if type(v2) is IntType:
            try:
                v = int(vars.get(k, None))
            except TypeError:
                v = v2
            vars[k] = v
    return vars
                
def insertVars():
    for k, v in defaultVars.items():
        sett = Settings(name=k, value=v, comment=k)
        sett.save()
# insertVars()
        

class Incoming(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    content = models.TextField(verbose_name=u'Содержание')
    created = models.DateTimeField(auto_now=True, verbose_name=u'Дата')
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = u"Входящие"
        verbose_name_plural = u"Входящие"
        ordering = ('-created',)

