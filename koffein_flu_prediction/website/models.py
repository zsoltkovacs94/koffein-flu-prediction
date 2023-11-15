from django.db import models
from datetime import datetime
from django.db.models import Q

# Create your models here.


class lekert_adatok(models.Model):
    WHOREGION = models.CharField("WHOREGION", max_length=10)
    COUNTRY_AREA_TERRITORY = models.TextField("COUNTRY_AREA_TERRITORY", max_length=255)
    ISO_YEAR = models.IntegerField("ISO_YEAR")
    ISO_WEEK = models.IntegerField("ISO_WEEK")
    ILI_CASE = models.IntegerField("ILI_CASE", blank=True, null=True)
    ILI_OUTPATIENTS = models.IntegerField("ILI_OUTPATIENTS", blank=True, null=True)
    SARI_CASE = models.IntegerField("SARI_CASE", blank=True, null=True)
    SARI_INPATIENTS = models.IntegerField("SARI_INPATIENTS", blank=True, null=True)


    def fluFilter(self, WHR = "Any", coarte = "Any", startDate = "1996-01-01", endDate = datetime.now().strftime("%Y-%m-%d")):
        data = lekert_adatok.objects.all()
        if(WHR != "Any"):
            data = data.filter(WHOREGION=WHR)
        if(coarte != "Any"):
            data = data.filter(COUNTRY_AREA_TERRITORY=coarte)
        try:
            sDate = datetime.strptime(startDate, '%Y-%m-%d')
        except ValueError:
            return generalt_adatok.objects.none()
        sYear = sDate.isocalendar().year
        sWeek = sDate.isocalendar().week
        try:
            eDate = datetime.strptime(endDate, '%Y-%m-%d')
        except ValueError:
            return generalt_adatok.objects.none()
        eYear = eDate.isocalendar().year
        eWeek = eDate.isocalendar().week
        f1 = Q(ISO_YEAR=sYear)
        f2 = Q(ISO_WEEK__gte=sWeek)
        f3 = Q(ISO_YEAR__gt=sYear)
        f4 = Q(ISO_YEAR=eYear)
        f5 = Q(ISO_WEEK__lte=eWeek)
        f6 = Q(ISO_YEAR__lt=eYear)
        return data.filter((f1 & f2) | f3).filter((f4 & f5) | f6).order_by("ISO_WEEK").order_by("ISO_YEAR")

class generalt_adatok(models.Model):
    WHOREGION = models.CharField("WHOREGION", max_length=10)
    COUNTRY_AREA_TERRITORY = models.TextField("COUNTRY_AREA_TERRITORY", max_length=255)
    ISO_YEAR = models.IntegerField("ISO_YEAR")
    ISO_WEEK = models.IntegerField("ISO_WEEK")
    ILI_CASE = models.IntegerField("ILI_CASE", blank=True, null=True)
    ILI_OUTPATIENTS = models.IntegerField("ILI_OUTPATIENTS", blank=True, null=True)
    SARI_CASE = models.IntegerField("SARI_CASE", blank=True, null=True)
    SARI_INPATIENTS = models.IntegerField("SARI_INPATIENTS", blank=True, null=True)

    def genFilter(self, WHR = "Any", coarte = "Any", startDate = "1996-01-01", endDate = datetime.now().strftime("%Y-%m-%d")):
        data = generalt_adatok.objects.all()
        if(WHR != "Any"):
            data = data.filter(WHOREGION=WHR)
        if(coarte != "Any"):
            data = data.filter(COUNTRY_AREA_TERRITORY=coarte)
        try:
            sDate = datetime.strptime(startDate, '%Y-%m-%d')
        except ValueError:
            return generalt_adatok.objects.none()
        sYear = sDate.isocalendar().year
        sWeek = sDate.isocalendar().week
        try:
            eDate = datetime.strptime(endDate, '%Y-%m-%d')
        except ValueError:
            return generalt_adatok.objects.none()
        eYear = eDate.isocalendar().year
        eWeek = eDate.isocalendar().week
        f1 = Q(ISO_YEAR=sYear)
        f2 = Q(ISO_WEEK__gte=sWeek)
        f3 = Q(ISO_YEAR__gt=sYear)
        f4 = Q(ISO_YEAR=eYear)
        f5 = Q(ISO_WEEK__lte=eWeek)
        f6 = Q(ISO_YEAR__lt=eYear)
        return data.filter((f1 & f2) | f3).filter((f4 & f5) | f6).order_by("ISO_WEEK").order_by("ISO_YEAR")
