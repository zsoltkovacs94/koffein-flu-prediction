from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .static import pager
from .static import prediction_handler
from .models import lekert_adatok, generalt_adatok

def home(request):
    return HttpResponseRedirect(reverse("tan"))

def gen(request):
    #print(prediction_handler.predict("ORSZÁGNÉV"))
    return render(request, 'index.html', {})

def tan(request):
    if(pager.showndata.count() == 0):
        pager.init(lekert_adatok.objects.all())
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
    """
    #Példa POST szűrés kezelés
    if request.method == 'POST' and 'filter' in request.POST:
        pager.init(lekert_adatok.filterByWHOREGION(lekert_adatok, request.POST.get('WHOREGION')))
    """
    database = pager.show()
    #database = lekert_adatok.objects.all()[:1000]
    return render(request, 'tanulo.html', {'all': database})
