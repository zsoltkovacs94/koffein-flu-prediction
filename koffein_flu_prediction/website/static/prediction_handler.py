import numpy
import datetime
from ..models import lekert_adatok
from ..models import generalt_adatok
from ..static import predictor
from django.db.models import Sum


def getData(coarte):
    if (coarte == ""):
        return 0
    length = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).count()
    last = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).order_by("ISO_WEEK").order_by("ISO_YEAR")[
           lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).count() - 1:]
    data = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).order_by("ISO_WEEK").order_by("ISO_YEAR")[
           length - 8:]
    pastIC = numpy.asarray([[a] for a in (IC[0] for IC in data.values_list("ILI_CASE"))]).transpose()
    pastIO = numpy.asarray([[a] for a in (IO[0] for IO in data.values_list("ILI_OUTPATIENTS"))]).transpose()
    pastSC = numpy.asarray([[a] for a in (SC[0] for SC in data.values_list("SARI_CASE"))]).transpose()
    pastSI = numpy.asarray([[a] for a in (SI[0] for SI in data.values_list("SARI_INPATIENTS"))]).transpose()
    newIC, newIO, newSC, newSI = predictor.prednext(pastIC, pastIO, pastSC, pastSI, 4)
    return (newIC, newIO, newSC, newSI, last.values_list("ISO_YEAR").get()[0], last.values_list("ISO_WEEK").get()[0])


def checkForPrevGen(WHOREGION, coarte, year, week):
    data = (generalt_adatok.objects.filter(WHOREGION=WHOREGION)
            .filter(COUNTRY_AREA_TERRITORY=coarte)
            .filter(ISO_YEAR=int(year))
            .filter(ISO_WEEK=int(week)))
    if not data:
        return 0
    else:
        return 1


def insert(WHOREGION, coarte, newIC, newIO, newSC, newSI, lastYear, lastWeek):
    skipped = 0
    for i in range(1, 5):
        numberOfWeeks = datetime.date(lastYear, 12, 31).isocalendar().week
        if ((lastWeek + i) <= numberOfWeeks):
            if (checkForPrevGen(WHOREGION, coarte, lastYear, lastWeek + i) == 1):
                skipped += 1
                continue
            generalt_adatok.objects.create(WHOREGION=WHOREGION,
                                           COUNTRY_AREA_TERRITORY=coarte,
                                           ISO_YEAR=lastYear,
                                           ISO_WEEK=(lastWeek + i),
                                           ILI_CASE=newIC[i - 1][0],
                                           ILI_OUTPATIENTS=newIO[i - 1][0],
                                           SARI_CASE=newSC[i - 1][0],
                                           SARI_INPATIENTS=newSI[i - 1][0]
                                           )
        else:
            if (checkForPrevGen(WHOREGION, coarte, lastYear + 1, lastWeek + i - numberOfWeeks) == 1):
                skipped += 1
                continue
            generalt_adatok.objects.create(WHOREGION=WHOREGION,
                                           COUNTRY_AREA_TERRITORY=coarte,
                                           ISO_YEAR=(lastYear + 1),
                                           ISO_WEEK=((lastWeek + i) - numberOfWeeks),
                                           ILI_CASE=newIC[i - 1][0],
                                           ILI_OUTPATIENTS=newIO[i - 1][0],
                                           SARI_CASE=newSC[i - 1][0],
                                           SARI_INPATIENTS=newSI[i - 1][0]
                                           )
    return skipped


def predict(coarte):
    country = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte)
    if not country:
        return "Nem létező ország"
    country = country[0]
    newIC, newIO, newSC, newSI, lastYear, lastWeek = getData(coarte)
    if (lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).aggregate(total=Sum('ILI_CASE'))['total'] == 0):
        newIC = numpy.asarray([[0], [0], [0], [0], [0], [0], [0], [0]])
    else:
        newIC = abs(newIC)
    if (lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).aggregate(total=Sum('ILI_OUTPATIENTS'))[
        'total'] == 0):
        newIO = numpy.asarray([[0], [0], [0], [0], [0], [0], [0], [0]])
    else:
        newIO = abs(newIO)
    if (lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).aggregate(total=Sum('SARI_CASE'))['total'] == 0):
        newSC = numpy.asarray([[0], [0], [0], [0], [0], [0], [0], [0]])
    else:
        newSC = abs(newSC)
    if (lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).aggregate(total=Sum('SARI_INPATIENTS'))[
        'total'] == 0):
        newSI = numpy.asarray([[0], [0], [0], [0], [0], [0], [0], [0]])
    else:
        newSI = abs(newSI)
    skipped = insert(country.WHOREGION, coarte, newIC, newIO, newSC, newSI, lastYear, lastWeek)
    return "Generálás sikeres " + skipped.__str__() + " insert átugorva"
