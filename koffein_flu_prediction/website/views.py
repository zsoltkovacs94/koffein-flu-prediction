from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .static import pager
from .static import prediction_handler
from .models import lekert_adatok, generalt_adatok
from datetime import datetime


def home(request):
    return HttpResponseRedirect(reverse("tan"))


def gen(request):
    szures = ['', '', '1996-01-01', (datetime.now() + relativedelta(months=1, days=14)).strftime("%Y-%m-%d")]
    if (pager.showndata.count() == 0 or not pager.isGen()):
        pager.init(generalt_adatok.objects.all(), gen=True)
    if request.method == 'POST' and 'back' in request.POST:
        pager.back()
        return HttpResponseRedirect(reverse("gen"))
    if request.method == 'POST' and 'backMore' in request.POST:
        pager.backMore()
        return HttpResponseRedirect(reverse("gen"))
    if request.method == 'POST' and 'forward' in request.POST:
        pager.forward()
        return HttpResponseRedirect(reverse("gen"))
    if request.method == 'POST' and 'forwardMore' in request.POST:
        pager.forwardMore()
        return HttpResponseRedirect(reverse("gen"))
    if request.method == 'POST' and 'filter' in request.POST:
        pager.init(generalt_adatok.genFilter(generalt_adatok,
                                             request.POST.get('WHOREGION'),
                                             request.POST.get('coarte'),
                                             request.POST.get('startDate'),
                                             request.POST.get('endDate')), gen=True)
        szures = [request.POST.get('WHOREGION'), request.POST.get('coarte'), request.POST.get('startDate'),
                  request.POST.get('endDate')]
    if request.method == 'POST' and 'reset' in request.POST:
        pager.init(generalt_adatok.objects.all(), gen=False)
        return HttpResponseRedirect(reverse("gen"))
    if request.method == 'POST' and 'setps' in request.POST:
        pager.setOnPage(request.POST.get('setps'))
    genmessage = ''
    if request.method == 'POST' and 'generate' in request.POST:
        genmessage = prediction_handler.predict(request.POST.get('gencoarte'))
        database = pager.init(generalt_adatok.objects.all(), gen=True)
    database = pager.show()
    print(szures)
    return render(request, 'index.html', {'current': database,
                                          'region': generalt_adatok.objects.all().values(
                                              'WHOREGION').distinct().order_by('WHOREGION'),
                                          'coarte': generalt_adatok.objects.all().values(
                                              'COUNTRY_AREA_TERRITORY').distinct().order_by('COUNTRY_AREA_TERRITORY'),
                                          'gencoarte': lekert_adatok.objects.all().values(
                                              'COUNTRY_AREA_TERRITORY').distinct().order_by('COUNTRY_AREA_TERRITORY'),
                                          'date': (datetime.now() + relativedelta(months=1, days=14)).strftime(
                                              "%Y-%m-%d"),
                                          'page': pager.getPage(),
                                          'maxpage': pager.getMaxPage(),
                                          'genmessage': genmessage,
                                          'szures': szures,
                                          'ps': pager.getOnPage()})


def tan(request):
    szures = ['', '', '1996-01-01', datetime.now().strftime("%Y-%m-%d")]
    if (pager.showndata.count() == 0 or pager.isGen()):
        pager.init(lekert_adatok.objects.all(), gen=False)
    if request.method == 'POST' and 'back' in request.POST:
        pager.back()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'backMore' in request.POST:
        pager.backMore()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'forward' in request.POST:
        pager.forward()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'forwardMore' in request.POST:
        pager.forwardMore()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'reset' in request.POST:
        pager.init(lekert_adatok.objects.all(), gen=False)
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'setps' in request.POST:
        pager.setOnPage(request.POST.get('setps'))
    # Példa POST szűrés kezelés
    if request.method == 'POST' and 'filter' in request.POST:
        pager.init(lekert_adatok.fluFilter(lekert_adatok,
                                           request.POST.get('WHOREGION'),
                                           request.POST.get('coarte'),
                                           request.POST.get('startDate'),
                                           request.POST.get('endDate')), gen=False)
        szures = [request.POST.get('WHOREGION'), request.POST.get('coarte'), request.POST.get('startDate'),
                  request.POST.get('endDate')]

    database = pager.show()
    # database = lekert_adatok.objects.all()[:1000]
    return render(request, 'tanulo.html', {'current': database,
                                           'region': lekert_adatok.objects.all().values(
                                               'WHOREGION').distinct().order_by('WHOREGION'),
                                           'coarte': lekert_adatok.objects.all().values(
                                               'COUNTRY_AREA_TERRITORY').distinct().order_by('COUNTRY_AREA_TERRITORY'),
                                           'date': datetime.now().strftime("%Y-%m-%d"),
                                           'page': pager.getPage(),
                                           'maxpage': pager.getMaxPage(),
                                           'szures': szures,
                                           'ps': pager.getOnPage()})
