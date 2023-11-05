from django.shortcuts import render
from .models import lekert_adatok

def home(request):
    return render(request, 'index.html', {})

def gen(request):
    return render(request, 'index.html', {})

def tan(request):
    database = lekert_adatok.objects.all()[:1000]
    return render(request, 'tanulo.html', {'all': database})
