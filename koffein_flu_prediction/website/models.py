from django.db import models

# Create your models here.


class lekert_adatok (models.Model):
    WHOREGION = models.CharField("WHOREGION", max_length=10)
    COUNTRY_AREA_TERRITORY = models.CharField("COUNTRY_AREA_TERRITORY", max_length=255)
    ISO_YEAR = models.IntegerField("ISO_YEAR")
    ISO_WEEK = models.IntegerField("ISO_WEEK")
    ILI_CASE = models.IntegerField("ILI_CASE")
    ILI_OUTPATIENTS = models.IntegerField("ILI_OUTPATIENTS")
    SARI_CASE = models.IntegerField("SARI_CASE")
    SARI_INPATIENTS = models.IntegerField("SARI_INPATIENTS")


class generalt_adatok(models.Model):
    WHOREGION = models.CharField("WHOREGION", max_length=10)
    COUNTRY_AREA_TERRITORY = models.CharField("COUNTRY_AREA_TERRITORY", max_length=255)
    ISO_YEAR = models.IntegerField("ISO_YEAR")
    ISO_WEEK = models.IntegerField("ISO_WEEK")
    ILI_CASE = models.IntegerField("ILI_CASE")
    ILI_OUTPATIENTS = models.IntegerField("ILI_OUTPATIENTS")
    SARI_CASE = models.IntegerField("SARI_CASE")
    SARI_INPATIENTS = models.IntegerField("SARI_INPATIENTS")

