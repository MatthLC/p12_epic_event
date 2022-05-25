from django.contrib import admin
from event_manager.models import Client, Contract, Event


admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
