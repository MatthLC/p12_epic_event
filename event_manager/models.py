from django.db import models
from django.conf import settings


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=64)
    mobile = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='EventContributor',
        related_name='event_contributions'
    )

    class Meta:
        unique_together = ('first_name', 'last_name', 'email')


class Contract(models.Model):
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey('event_manager.Client', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now=True)


class Event(models.Model):
    OPENED = 'OPENED'
    CLOSED = 'CLOSED'
    INCOMING = 'INCOMING'

    STATUS_CHOICE = [
        (OPENED, 'opened'),
        (CLOSED, 'closed'),
        (INCOMING, 'incoming'),
    ]

    client = models.ForeignKey('event_manager.Client', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_status = models.CharField(max_length=32, choices=STATUS_CHOICE)
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(max_length=1024, blank=True)


class EventContributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_contributor')
    client = models.ForeignKey('event_manager.Client', on_delete=models.CASCADE, related_name='contributor_event')
    event_id = models.IntegerField()

    class Meta:
        unique_together = ('user', 'client', 'event_id')
