from django.db import models

# Create your models here.
class dataFlight(models.Model):
    hex = models.CharField(verbose_name='ICAO', max_length=255, null=True, blank=True)
    squawk = models.CharField(max_length=255, null=True, blank=True)
    flight = models.CharField(verbose_name="Flight Code", max_length=255, null=True, blank=True)
    lat  = models.FloatField(verbose_name="Latitude", null=True, blank=True)
    lon = models.FloatField(verbose_name="Longitude", null=True, blank=True)
    validposition = models.IntegerField(null=True, blank=True)
    altitude = models.IntegerField(null=True, blank=True)
    vert_rate = models.IntegerField(null=True, blank=True)
    track = models.IntegerField(null=True, blank=True)
    validtrack = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    messages = models.IntegerField(null=True, blank=True)
    seen = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.flight} valid : {self.validposition}'