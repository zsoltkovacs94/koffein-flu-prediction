import numpy

from ..models import lekert_adatok
from ..models import generalt_adatok
from ..static import predictor


def getData(coarte):
    if(coarte == ""):
        return 0
    length = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).count()
    last = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).order_by("ISO_WEEK").order_by("ISO_YEAR")[lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).count()-1:]
    data = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte).order_by("ISO_WEEK").order_by("ISO_YEAR")[length-8:]
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
    for i in range(0, 4):
        if((lastWeek+i) < 54):
            if(checkForPrevGen(WHOREGION, coarte,lastYear,lastWeek+i) == 1):
                return
            generalt_adatok.objects.create(WHOREGION=WHOREGION,
                                           COUNTRY_AREA_TERRITORY=coarte,
                                           ISO_YEAR=lastYear,
                                           ISO_WEEK=(lastWeek + i),
                                           ILI_CASE=newIC[i][0],
                                           ILI_OUTPATIENTS=newIO[i][0],
                                           SARI_CASE=newSC[i][0],
                                           SARI_INPATIENTS=newSI[i][0]
                                           )
        else:
            if(checkForPrevGen(WHOREGION, coarte,lastYear+1,lastWeek+i-53) == 1):
                return
            generalt_adatok.objects.create(WHOREGION=WHOREGION,
                                           COUNTRY_AREA_TERRITORY=coarte,
                                           ISO_YEAR=(lastYear + 1),
                                           ISO_WEEK=((lastWeek + i)-53),
                                           ILI_CASE=newIC[i][0],
                                           ILI_OUTPATIENTS=newIO[i][0],
                                           SARI_CASE=newSC[i][0],
                                           SARI_INPATIENTS=newSI[i][0]
                                           )

def predict(coarte):
    country = lekert_adatok.objects.filter(COUNTRY_AREA_TERRITORY=coarte)[0]
    newIC, newIO, newSC, newSI, lastYear, lastWeek = getData(coarte)
    insert(country.WHOREGION, coarte, newIC, newIO, newSC, newSI, lastYear, lastWeek)
