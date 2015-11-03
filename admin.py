from models import Station, NeerslagStation, MeteoData
from django.contrib.gis import admin

class StationAdmin(admin.OSMGeoAdmin):
    model = Station
    search_fields = ['naam',]
    list_display = ('naam', 'nummer','coords')
    
admin.site.register(Station,StationAdmin)
admin.site.register(NeerslagStation,StationAdmin)
#test commentaar