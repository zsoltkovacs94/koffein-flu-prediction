from ..models import lekert_adatok
from ..models import generalt_adatok
from .. import urls


def getAllData(path):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        allData = lekert_adatok.objects.all()
    elif (path == urls.urlpatterns[1]):
        allData = generalt_adatok.objects.all()

    return allData


def filterByWHORegion(path, whoRegion):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredWHORegion = lekert_adatok.objects.filter(WHOREGION=whoRegion)
    elif (path == urls.urlpatterns[1]):
        filteredWHORegion = generalt_adatok.objects.filter(WHOREGION=whoRegion)

    return filteredWHORegion


def filterByCoarte(path, coarte):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredCoarte = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte)
    elif (path == urls.urlpatterns[1]):
        filteredCoarte = generalt_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte)

    return filteredCoarte


def filterByYear(path, isoYear):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredYear = lekert_adatok.objects.filter(ISO_YEAR=isoYear)
    elif (path == urls.urlpatterns[1]):
        filteredYear = generalt_adatok.objects.filter(ISO_YEAR=isoYear)

    return filteredYear


def filterByTime(path, isoYear, isoWeek):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredTime = lekert_adatok.objects.filter(ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    elif (path == urls.urlpatterns[1]):
        filteredTime = generalt_adatok.objects.filter(ISO_YEAR=isoYear, ISO_WEEL=isoWeek)

    return filteredTime


def filterByWHORegionAndYear(path, whoRegion, isoYear):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredWHOYear = lekert_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear)
    elif (path == urls.urlpatterns[1]):
        filteredWHOYear = generalt_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear)

    return filteredWHOYear


def filterByWHORegionAndTime(path, whoRegion, isoYear, isoWeek):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredWHOTime = lekert_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    elif (path == urls.urlpatterns[1]):
        filteredWHOTime = generalt_adatok.objects.filter(WHOREGION=whoRegion, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)

    return filteredWHOTime


def filterByCoarteAndYear(path, coarte, isoYear):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredCoarteYear = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear)
    elif (path == urls.urlpatterns[1]):
        filteredCoarteYear = generalt_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear)

    return filteredCoarteYear


def filterByCoarteAndTime(path, coarte, isoYear, isoWeek):
    if (path == urls.urlpatterns[0] or path == urls.urlpatterns[2]):
        filteredCoarteTime = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)
    elif (path == urls.urlpatterns[1]):
        filteredCoarteTime = generalt_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte, ISO_YEAR=isoYear, ISO_WEEK=isoWeek)

    return filteredCoarteTime