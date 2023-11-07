import numpy

from ..models import lekert_adatok
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


def predict(coarte):
    newIC, newIO, newSC, newSI, lastYear, lastWeek = getData(coarte)
