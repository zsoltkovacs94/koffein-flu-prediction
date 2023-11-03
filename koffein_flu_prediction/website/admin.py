from django.contrib import admin
from .models import lekert_adatok
from .models import generalt_adatok

admin.site.register(lekert_adatok)
admin.site.register(generalt_adatok)

# Register your models here.
