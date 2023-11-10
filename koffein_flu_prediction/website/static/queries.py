from ..models import lekert_adatok
from ..models import generalt_adatok
from .. import urls

def getAllData(path):
    if(path == urls.urlpatterns[0] | path == urls.urlpatterns[2]):
        allData = lekert_adatok.objects.all()
    elif(path == urls.urlpatterns[1]):
        allData = generalt_adatok.objects.all()

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


def filterByWHORegionAndYear(whoRegion, isoYear):
    filteredWHOYear = lekert_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear)
    return filteredWHOYear


def filterByWHORegionAndTime(whoRegion, isoYear, isoWeek):
    filteredWHOTime = lekert_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    return filteredWHOTime


def filterByCoarteAndYear(coarte, isoYear):
    filteredCoarteYear = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear)
    return filteredCoarteYear


def filterByCoarteAndTime(coarte, isoYear, isoWeek):
    filteredCoarteTime = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    return filteredCoarteTime