from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def gen(request):
    return render(request, 'index.html', {})

def tan(request):
    return render(request, 'tanulo.html', {})
