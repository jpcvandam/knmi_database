from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from .util import closest as closestn
WGS84 = 4326
RDNEW = 28992

class Station(models.Model):
    nummer = models.IntegerField()
    naam = models.CharField(max_length=50)
    location = models.PointField(srid=RDNEW)
    objects = models.GeoManager()
    
    def coords(self):
        return (self.location.x, self.location.y)
    coords.short_description = 'Coordinaten'
                
    def __unicode__(self):
        return self.naam
    
    @classmethod
    def closest(cls, coords, n=1):
        ''' coords in rdnew projection ''' 
        return closestn(cls,coords,n)

    class Meta:
        ordering = ('naam',)

class NeerslagStation(models.Model):
    nummer = models.IntegerField()
    naam = models.CharField(max_length=50)
    location = models.PointField(srid=RDNEW)
    objects = models.GeoManager()
            
    def coords(self):
        return (self.location.x, self.location.y)
    coords.short_description = 'Coordinaten'

    def __unicode__(self):
        return self.naam

    @classmethod
    def closest(cls, coords, n=1):
        ''' coords in rdnew projection ''' 
        return closestn(cls,coords,n)

    class Meta:
        ordering = ('naam',)


class MeteoData(models.Model):
	nummer = models.IntegerField()
	datum = models.DateTimeField()
	rh = models.IntegerField()
	ev24 = models.IntegerField()