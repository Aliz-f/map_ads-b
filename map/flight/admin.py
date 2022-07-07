from django.contrib import admin
from .models import dataFlight
# Register your models here.
# admin.site.register(dataFlight)

@admin.register(dataFlight)
class flightAdmin(admin.ModelAdmin):
    list_display = [
        "flight",
        "hex",
        "validposition",
        "lat",
        "lon",
        "altitude",
        "speed",
    ]