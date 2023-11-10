from django.db import models

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


class generalt_adatok(models.Model):
    WHOREGION = models.CharField("WHOREGION", max_length=10)
    COUNTRY_AREA_TERRITORY = models.TextField("COUNTRY_AREA_TERRITORY", max_length=255)
    ISO_YEAR = models.IntegerField("ISO_YEAR")
    ISO_WEEK = models.IntegerField("ISO_WEEK")
    ILI_CASE = models.IntegerField("ILI_CASE", blank=True, null=True)
    ILI_OUTPATIENTS = models.IntegerField("ILI_OUTPATIENTS", blank=True, null=True)
    SARI_CASE = models.IntegerField("SARI_CASE", blank=True, null=True)
    SARI_INPATIENTS = models.IntegerField("SARI_INPATIENTS", blank=True, null=True)


def getAllData():
    allData = lekert_adatok.objects.all()
    return allData


def filterByWHORegion(whoRegion):
    filteredWHORegion = lekert_adatok.objects.filter(WHOREGION=whoRegion)
    return filteredWHORegion


def filterByCoarte(coarte):
    filteredCoarte = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte)
    return filteredCoarte


def filterByYear(isoYear):
    filteredYear = lekert_adatok.objects.filter(ISO_YEAR=isoYear)
    return filteredYear


def filterByTime(isoYear, isoWeek):
    filteredTime = lekert_adatok.objects.filter(ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    return filteredTime


def filterByWHORegionAndTime(whoRegion, isoYear, isoWeek):
    filteredWHOTime = lekert_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    return filteredWHOTime


def filterByCoarteAndTime(coarte, isoYear, isoWeek):
    filteredCoarteTime = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    return filteredCoarteTime