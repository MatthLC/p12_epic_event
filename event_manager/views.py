from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException

from event_manager.models import Client, Contract, Event, EventContributor
from event_manager.serializers import (
    ClientListSerializer, ClientDetailsSerializer,
    ContractListSerializer, ContractDetailsSerializer,
    EventListSerializer, EventDetailsSerializer,
)

from event_manager.permissions import IsClientManager, IsContractManager, IsEventManager

from django_filters.rest_framework import DjangoFilterBackend


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailsSerializer
    permission_classes = [IsClientManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name', 'email']

    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['MANAGER', 'SALES']).exists():
            return Client.objects.all()

        elif self.request.user.groups.filter(name__in=['SUPPORT']).exists():
            return Client.objects.filter(contributors=self.request.user).distinct()

        else:
            raise PermissionDenied

    def perform_update(self, serializer):
        if self.request.user.groups.filter(name='MANAGER').exists():
            serializer.save()

        elif (
            self.request.user.groups.filter(name__in=['SALES']).exists()
            and self.get_object().sales_contact == self.request.user
        ):
            serializer.save()

        else:
            raise PermissionDenied


class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailsSerializer
    permission_classes = [IsContractManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'date_created', 'amount']

    def get_queryset(self):
        return Contract.objects.all()

    def perform_update(self, serializer):
        if self.request.user.groups.filter(name='MANAGER').exists():
            serializer.save()

        elif (
            self.request.user.groups.filter(name__in=['SALES']).exists()
            and self.get_object().sales_contact == self.request.user
        ):

            serializer.save()

        else:
            raise PermissionDenied


class EventViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailsSerializer
    permission_classes = [IsEventManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'event_date']

    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['MANAGER', 'SALES']).exists():
            return Event.objects.all()

        elif self.request.user.groups.filter(name__in=['SUPPORT']).exists():
            return Event.objects.filter(support_contact=self.request.user)

        else:
            raise PermissionDenied

    def perform_create(self, serializer):
        client_id = serializer.validated_data['client'].id
        is_contract_signed = Contract.objects.filter(client=client_id, status=True)

        if is_contract_signed:
            event = serializer.save()
            client = get_object_or_404(Client, id=event.client.id)
            EventContributor.objects.create(
                user=event.support_contact,
                client=client,
                event_id=event.id
            )
        else:
            raise APIException("The client does not own contract yet.")

    def perform_update(self, serializer):
        old_event_status = self.get_object().event_status
        if old_event_status == 'CLOSED':
            raise APIException("This event is closed.")
        else:
            old_event = self.get_object().id
            old_support_contact_to_remove = Event.objects.get(id=old_event).support_contact.id

            event = serializer.save()
            client = get_object_or_404(Client, id=event.client.id)

            EventContributor.objects.filter(user=old_support_contact_to_remove, event_id=event.id).delete()
            EventContributor.objects.create(
                user=event.support_contact,
                client=client,
                event_id=event.id
            )