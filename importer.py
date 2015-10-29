from models import NeerslagStation, Station, MeteoData
from django.contrib.gis.geos import Point
from dateutil import parser

WGS84 = 4326
RDNEW = 28992


def importneerslag(fil):
    with open(fil) as f:
        f.readline()
        line = f.readline()
        while line != '':
            words = line.split(',')
            if len(words)> 4:
				x = float(words[1])
				y = float(words[2])
				target = Point(x,y, srid=WGS84)
				target.transform(RDNEW)
				NeerslagStation.objects.get_or_create(
                    naam = words[4],
                    nummer = int(words[0]),					
					#target.transform(RDNEW)
                    #zipfilename = words[2],
                    location = target
                )
            line = f.readline()
################################################################################
#Meteodata uit de tekstbestandjes importeren
################################################################################

def importdata(fil):
    with open(fil) as f:
		f.readline()        
		line = f.readline()
		while line !='':
			words = line.split(',')
			if len(words)> 7 and words[0]!='# STN'and words[8]!='':
				MeteoData.objects.get_or_create(
					nummer = int(words[0]),
					datum = parser.parse(words[1]),
					rh = int(words[2]),
					ev24 = int(words[8])
                )
			line = f.readline()			    
    


def importall():
    NeerslagStation.objects.all().delete()
    importneerslag('/home/john/ftm/ftm/ftm/data/KNMI_meteostations.csv')


def import_geg():
	MeteoData.objects.all().delete()
	for i in  [215]:#[215, 225, 235, 240, 242, 249, 251, 257, 260, 265, 267, 269, 270, 273, 275, 277, 278, 279, 280, 283, 286, 290, 310, 323,  319, 330, 340, 344, 348, 350, 356, 370, 375, 377, 380, 391,  ]:
		importdata('/home/john/ftm/ftm/ftm/data/METEO'+str(i)+'.TXT')
