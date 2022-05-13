from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from event_manager.models import Client, Contract, Event
from authentication.models import User
from django.shortcuts import get_object_or_404
from datetime import datetime


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'sales_contact'
        ]

    def validate(self, data):

        user = get_object_or_404(User, id=data['sales_contact'].id)
        if user.groups.filter(name='SALES').exists():
            return data
        else:
            raise serializers.ValidationError('Your contact does not belong to the sales team')


class ClientDetailsSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'date_created',
            'date_updated',
            'sales_contact',
        ]


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status', 'amount']

    def validate(self, data):
        user = get_object_or_404(User, id=data['sales_contact'].id)
        if user.groups.filter(name='SALES').exists():
            return data
        else:
            raise serializers.ValidationError('Your contact does not belong to the sales team')

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError('Amount must be egual or superior to 0.')
        else:
            return value


class ContractDetailsSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'sales_contact',
            'client',
            'amount',
            'status',
            'date_created',
            'date_updated',
            'payment_due'
        ]


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'client', 'event_status', 'event_date', 'support_contact', 'attendees', 'notes']

    def validate(self, data):
        user = get_object_or_404(User, id=data['support_contact'].id)
        if user.groups.filter(name=['SUPPORT']).exists():
            return data
        else:
            raise serializers.ValidationError('Your contact does not belong to the support team')

    def validate_event_date(self, value):
        USER_DATETIME = datetime.now().strftime("%Y-%m-%d")
        if USER_DATETIME > str(value):
            raise serializers.ValidationError('Check the date of the event. Yesterday is not tomorrow.')
        else:
            return value

    def validate_attendees(self, value):
        if value < 0:
            raise serializers.ValidationError('Attendees must be egual or superior to 0.')
        else:
            return value


class EventDetailsSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'client',
            'event_status',
            'event_date',
            'support_contact',
            'date_created',
            'date_updated',
            'attendees',
            'notes'
        ]
