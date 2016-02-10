# -*- coding: utf-8 -*- 

import math, random

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import Context
from django.core.mail import send_mail
from django.template.loader import get_template

from models import *
from forms import *

####################################################################################################
## stuff
####################################################################################################

def toInt(*args):
    result = []
    for x in args:
        if x:
            result.append(int(x))
        else:
            result.append(0)
    return result

def renderToResponse(request, template, vars, mimetype=None):
    for k, v in getVars().items():
        vars[k] = v
    
    vars['menuTop'] = MenuTop.objects.all()
    vars['menuBottom'] = MenuBottom.objects.all()
    vars['menuStart'] = MenuStart.objects.all()
    vars['aboutPageList'] = getAboutPageList()
    widget = vars.get('widget', '|1234').split('|')+['', '']
    vars['widget'] = dict([(v, True) for v in widget[0]])
    vars['widgetR'] = dict([(v, True) for v in widget[1]])
    numTypeList = NumberType.objects.all()
    nums = [Number.objects.filter(type=t).order_by('id') for t in numTypeList]
    nums = [random.choice(n) for n in nums if n]
    vars['rndNumbers'] = nums
    if ')' in vars['contactPhone']:
        vars['preContactPhone'], vars['contactPhone'] = vars['contactPhone'].split(')')
        vars['preContactPhone'] += ')'
    if mimetype:
        return render_to_response(template, vars, mimetype=mimetype)
    else:
        return render_to_response(template, vars)

def pager(items, curPage, pageSize):
    # curPage: 1, 2, 3...
    curPage = int(curPage)
    pageCount = (len(items)+pageSize-1)//pageSize
    pageList = xrange(1, pageCount+1)
    items = items[(curPage-1)*pageSize:curPage*pageSize]
    return curPage, pageCount, pageList, items

def emailTemplate(emailFrom, emailTo, tmplFile, vars):
    emailFrom = 'gravitel.ru@gmail.com'
    t = get_template(tmplFile)
    s = t.render(Context(vars))
    subject, body = s.split('\n', 1)
    subject = subject.strip()
    body = body.strip()
    # send_mail(subject, body, emailFrom, [emailTo], fail_silently=False)
    i = Incoming(title=subject, content=body)
    i.save()
    return 'mail "%s" => "%s"\n%s\n%s\n%s' % (emailFrom, emailTo, subject, '-'*30, body)
    
def getPage(url):
    return get_object_or_404(Page, url=url)

def getPageList(urlList):
    return [i for i in Page.objects.all() if i.url in urlList]

def getAboutPageList():
    urlList = ('/about/', '/news/', '/partners/', '/certificates/', '/contact/')
    return getPageList(urlList)

####################################################################################################
## admin
####################################################################################################

def adminJs(request):
    ref = request.META.get('HTTP_REFERER', '')
    try:
        url = ref.split('grmain/')[1].split('/')[0]
    except Exception, e:
        url = str(e)
    
    return render_to_response('admin/admin.js', locals())

####################################################################################################
## pages
####################################################################################################

def index(request):
    page = getPage('/')
    partnerList = Client.objects.all()[:6]
    bannerList = Banner.objects.all()
    banner2List = Banner2.objects.all()
    widget = '14|3'
    return renderToResponse(request, 'index.html', locals())

def profit(request):
    page = getPage('/profit/')
    return renderToResponse(request, 'profit.html', locals())

def siteMap(request):
    services = Service.objects.all()
    payment = Payment.objects.all()
    productCats = ProductCat.objects.all()
    helpCats = HelpCat.objects.all()
    videos = [i for i in services if i.video]
    about = getAboutPageList()
    widget = '|14'
    return renderToResponse(request, 'site-map.html', locals())

def login(request, id=None):
    VARS = getVars()
    widget = '|'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            vars = form.cleaned_data
            # emailDump = emailTemplate(VARS['contactEmailQuestion'], VARS['contactEmailQuestion'], 'order.txt', vars)
    else:
        form = LoginForm()
    return renderToResponse(request, 'login.html', locals())

####################################################################################################
## about
####################################################################################################

def renderAbout(request, url, template, vars=None):
    if not vars:
        vars = {}
    vars['ulUrl'] = url
    vars['page'] = getPage(url)
    return renderToResponse(request, template, vars)

def about(request):
    items = Employee.objects.all()
    return renderAbout(request, '/about/', 'about.html', locals())
    
def news(request, curPage=1):
    VARS = getVars()
    items = News.objects.all()
    curPage, pageCount, pageList, items = pager(items, curPage, VARS['perPageNews'])
    return renderAbout(request, '/news/', 'about-news.html', locals())

def certificates(request):
    items = Certificate.objects.all()
    return renderAbout(request, '/certificates/', 'about-certificates.html', locals())

def partners(request):
    partnerList = Partner.objects.all()
    clientList = Client.objects.all()
    return renderAbout(request, '/partners/', 'about-partners.html', locals())

def contact(request):
    return renderAbout(request, '/contact/', 'base-about.html')
    
####################################################################################################
## service
####################################################################################################

def services(request, url=None, isVideo=None):
    ulItems = Service.objects.all()
    ulRoot = '/services/'
    ulUrl = url
    if url:
        i = get_object_or_404(Service, url=url)
        return renderToResponse(request, 'services.html', locals())
    else:
        page = getPage('/services/')
        return renderToResponse(request, 'base-services.html', locals())

def video(request, url=None):
    ulItems = [i for i in Service.objects.all() if i.video]
    ulRoot = '/video/'
    ulUrl = url
    if url:
        i = get_object_or_404(Service, url=url)
        widget = '|1'
        return renderToResponse(request, 'video.html', locals())
    else:
        page = getPage('/video/')
        widget = '|123'
        return renderToResponse(request, 'base-video.html', locals())

def presentation(request):
    ulItems = Service.objects.all()
    ulRoot = '/services/'
    page = getPage('/presentation/')
    return renderToResponse(request, 'base-services.html', locals())

####################################################################################################
## 
####################################################################################################

def help(request, catUrl=None, subcatUrl=None, curPage=1):
    VARS = getVars()

    cat = subcat = None
    if catUrl:
        cat = get_object_or_404(HelpCat, url=catUrl)
    if subcatUrl:
        subcat = get_object_or_404(HelpSubcat, url=subcatUrl, cat=cat)
    catList = HelpCat.objects.all()
    
    if cat:
        subcatList = HelpSubcat.objects.filter(cat=cat)
        if subcat:
            items = Help.objects.filter(subcat=subcat)
        else:
            items = []
            for i in subcatList:
                items += Help.objects.filter(subcat=i)
        curPage, pageCount, pageList, items = pager(items, curPage, VARS['perPageHelp'])
        if len(subcatList) <= 1:
            subcatList = []
        
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            vars = form.cleaned_data
            subject = [v for k, v in getSubjectChoices() if k == vars['subject']]
            vars['subject'] = subject[0]
            emailDump = emailTemplate(vars['email'], VARS['contactEmailQuestion'], 'help.txt', vars)
    else:
        form = QuestionForm()
        
    widget = '|1'
    
    return renderToResponse(request, 'help.html', locals())

def catAjax(request, catId, curPage=1):
    VARS = getVars()

    cat = get_object_or_404(ProductCat, id=catId)
    items = Product.objects.filter(cat=cat)
    curPage, pageCount, pageList, items = pager(items, curPage, VARS['perPageProduct'])
    return renderToResponse(request, 'cat-ajax.html', locals())

def products(request, catUrl=None, curPage=1):
    VARS = getVars()
    
    cat = None
    if catUrl:
        cat = get_object_or_404(ProductCat, url=catUrl)
    catList = ProductCat.objects.all()
    
    if cat:
        items = Product.objects.filter(cat=cat)
    else:
        items = Product.objects.all()
    curPage, pageCount, pageList, items = pager(items, curPage, VARS['perPageProduct'])
    
    ulItems = catList
    ulRoot = '/catalog/'
    ulUrl = catUrl
    
    return renderToResponse(request, 'product-list.html', locals())

def product(request, id):
    i = get_object_or_404(Product, id=id)
    items = ProductCat.objects.all()
    
    ulItems = items
    ulRoot = '/catalog/'
    ulUrl = i.cat.url
    
    return renderToResponse(request, 'product.html', locals())

def order(request, id):
    VARS = getVars()

    i = get_object_or_404(Product, id=id)
    catList = ProductCat.objects.all()
    
    catUrl = i.cat.url
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            vars = form.cleaned_data
            vars['i'] = i
            emailDump = emailTemplate(VARS['contactEmailOrder'], VARS['contactEmailOrder'], 'order.txt', vars)
    else:
        form = OrderForm()
        
    return renderToResponse(request, 'order.html', locals())

def payment(request, url=None):
    items = Payment.objects.all()
    ulItems = items
    ulRoot = '/payment/'
    ulUrl = url
    # widget = '|1'
    if url:
        i = get_object_or_404(Payment, url=url)
        return renderToResponse(request, 'payment.html', locals())
    else:
        page = getPage('/payment/')
        return renderToResponse(request, 'payment-list.html', locals())

####################################################################################################
## phone
####################################################################################################

def tariffs(request, url=None, url2=None):
    widget = '|14'

    if url == 'calls':
        if not url2:
            url2 = 'russia'
        m = { 'russia': CallRussia, 'sng': CallSng, 'foreign': CallForeign }[url2]
        items = m.objects.all()
        return renderToResponse(request, 'tariffs-calls.html', locals())

    if url == 'numbers':
        typeList = NumberType.objects.all()
        if url2:
            type = get_object_or_404(NumberType, url=url2)
        else:
            type = typeList[0]
        url2 = type.url
        items = Number.objects.filter(type=type)
        return renderToResponse(request, 'tariffs-numbers.html', locals())

    return renderToResponse(request, 'tariffs.html', locals())

####################################################################################################
## wizard
####################################################################################################

def wizard(request):
    widget = '|'
    typeList = NumberType.objects.all()
    catList = ProductCat.objects.all()
    for t in typeList:
        t.numberList = Number.objects.filter(type=t)
    return renderToResponse(request, 'wizard.html', locals())
    
def wizardSummary(request, numbers, persons, fax, email, lines, catalog, fileName, type=False): #fileName - temp
    VARS = getVars()
    
    numSum = 0
    prodSum = 0
    
    persons, lines, fax, email = toInt(persons, lines, fax, email)
    linesSum = int(math.ceil(float(persons)/4))
    linesSum = max(linesSum, 2)+lines
    
    if numbers:
        numbers = [int(i) for i in numbers.split(',')]
        numberTypeList = NumberType.objects.all()
        for i, v in enumerate(numberTypeList):
            v.numbers = Number.objects.filter(type=v, id__in=numbers)
            numSum += v.price*len(v.numbers)
        numberTypeList = [i for i in numberTypeList if i.numbers]
    
    if catalog:
        productList = []
        for i in catalog.split(','):
            id, count = i.split(':')
            id = int(id)
            count = int(count)
            p = Product.objects.get(id=id)
            p.count = count
            p.allPrice = p.price*count
            productList.append(p)
            prodSum += p.allPrice
        
    monthSum = persons*VARS['pricePerson']
    if fax: monthSum += persons*VARS['priceFax']
    if email: monthSum += persons*VARS['priceEmail']
    if numbers: monthSum = max(monthSum, len(numbers)*1000)
    monthSum += lines*VARS['priceLine']
    
    sum = prodSum+numSum+monthSum
    
    widget = '|'
    
    if not type:
        return renderToResponse(request, 'wizard-summary.html', locals())
    elif type == 'doc':
        return renderToResponse(request, 'wizard-summary-doc.html', locals(), mimetype='application/msword')
    elif type == 'html':
        return renderToResponse(request, 'wizard-summary-doc.html', locals())
    
####################################################################################################
## wizard
####################################################################################################

def _install(request):
    data = [
        # User(username='beh', email='rdoroshko@gmail.com', password='ser ver 2', is_superuser=True, is_staff=True),
        # User(username='admin', email='admin@gravitel.ru', password='123', is_superuser=False, is_staff=True),
        Page(url='/', title=u'Гравител', content='<h1>Гравител</h1>', sort_no=0),
        Page(url='/services/', title=u'Сервисы', content='<h1>Сервисы</h1>', sort_no=0),
        Page(url='/video/', title=u'Видео-файлы', content='<h1>Видео-файлы</h1>', sort_no=0),
        Page(url='/profit/', title=u'Выгоды', content='<h1>Выгоды</h1>', sort_no=0),
        Page(url='/presentation/', title=u'Презентация', content='<h1>Презентация</h1>', sort_no=0),
        
        Page(url='/about/', title=u'Наша компания', content='<h1>Наша компания</h1>', sort_no=1),
        Page(url='/news/', title=u'Новости', content='<h1>Новости</h1>', sort_no=2),
        Page(url='/partners/', title=u'Партнеры и клиенты', content='<h1>Партнеры и клиенты</h1>', sort_no=3),
        Page(url='/certificates/', title=u'Лицензии', content='<h1>Лицензии</h1>', sort_no=4),
        Page(url='/contact/', title=u'Контактная информация', content='<h1>Контактная информация</h1>', sort_no=5),
        
        MenuTop(url='/catalog/', title=u'Оборудование', sort_no=1),
        MenuTop(url='/help/', title=u'Помощь', sort_no=2),
        MenuTop(url='/video/', title=u'Видео-файлы', sort_no=3),
        MenuTop(url='/contact/', title=u'Контактная информация', sort_no=4),

        MenuBottom(url='/about/', title=u'Кто мы?', sort_no=1),
        MenuBottom(url='/certificates/', title=u'Лицензии и сертификаты', sort_no=2),
        MenuBottom(url='/news/', title=u'Новости', sort_no=3),
        MenuBottom(url='/partners/', title=u'Клиенты и партнеры', sort_no=4),
        
        MenuStart(url='/presentation/', title=u'Посмотреть ролик с презентацией', sort_no=2),
        MenuStart(url='/help/', title=u'Посмотреть часто задаваемые вопросы', sort_no=3),
        MenuStart(url='/wizard/', title=u'Запустить мастер подбора услуги', sort_no=4),
        MenuStart(url='/docs/dictionary.pdf', title=u'Скачать справочник клиента', sort_no=5),
        
        NumberType(url='classic', title=u'Классический', price=1000, sort_no=1),
        NumberType(url='gold', title=u'Золотой', price=3000, sort_no=2),
        NumberType(url='vip', title=u'VIP', price=10000, sort_no=3),
    ]
    
    items = []
    for i in data:
        try:
            i.save()
            items.append(i)
        except Exception, e:
            items.append(e)
    
    # user = User.objects.create_user(username='beh', email='rdoroshko@gmail.com', password='ser ver 2')
    # user.is_superuser = True
    # user.is_staff = True
    # user.save()
    # items += [user]
    
    # for s in '/|/services/|/video/|/profit/|/about/|/news/|/certificates/|/partners/|/contact/|/presentation/'.split('|'):
    
    return render_to_response('_install.html', locals())

def _404(request):
    return render_to_response('404.html', locals())

