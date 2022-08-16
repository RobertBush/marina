from django.contrib import admin
from marina.power.models import Boat, Engine, BoatEngine

admin.site.register(Boat)
admin.site.register(Engine)
admin.site.register(BoatEngine)
