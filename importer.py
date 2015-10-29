from models import NeerslagStation, Station
from django.contrib.gis.geos import Point
WGS84 = 4326
RDNEW = 28992


def importneerslag(fil):
    with open(fil) as f:
        f.readline()
        line = f.readline()
        while line != '':
            words = line.split(',')
            if len(words)>4:
                x = float(words[1])
                y = float(words[2])
				target = Point(x,y, srid=WGS84)
				target.transform(RDNEW)
                NeerslagStation.objects.get_or_create(
                    naam = words[4],
                    nummer = int(words[0]),
                    #zipfilename = words[2],
                    location = target#Point(x,y)
                )
            line = f.readline()

			    
    

def importstations(fil):
    with open(fil) as f:
        f.readline()
        line = f.readline()
        while line != '':
            words = line.split(',')
            if len(words)>4:
                x = float(words[1])
                y = float(words[2])
				target = Point(x,y, srid=WGS84)
				target.transform(RDNEW)
                Station.objects.get_or_create(
                    nummer = int(words[0]),
                    naam = words[4],
                    #zipfilename = words[2],
                    location = Point(x,y)
                )
            line = f.readline()

def importall():
    NeerslagStation.objects.all().delete()
    importneerslag('/home/john/ftm/ftm/ftm/data/KNMI_meteostations.csv')
    Station.objects.all().delete()
    importstations('/home/john/ftm/ftm/ftm/data/KNMI_meteostations.csv')
