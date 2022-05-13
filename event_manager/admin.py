from django.contrib import admin
from event_manager.models import Client, Contract, Event, EventContributor
# Register your models here.

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(EventContributor)
