from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .static import tanuloPager
from .static import prediction_handler

def home(request):
    return HttpResponseRedirect(reverse("tan"))

def gen(request):
    #prediction_handler.predict("VALAMI ORSZÁGNÉV")
    return render(request, 'index.html', {})

def tan(request):
    if request.method == 'POST' and 'back' in request.POST:
        tanuloPager.back()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'backMore' in request.POST:
        tanuloPager.backMore()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'forward' in request.POST:
        tanuloPager.forward()
        return HttpResponseRedirect(reverse("tan"))
    if request.method == 'POST' and 'forwardMore' in request.POST:
        tanuloPager.forwardMore()
        return HttpResponseRedirect(reverse("tan"))
    database = tanuloPager.show()
    #database = lekert_adatok.objects.all()[:1000]
    return render(request, 'tanulo.html', {'all': database})
