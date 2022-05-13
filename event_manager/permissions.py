from rest_framework.permissions import BasePermission
from authentication.models import User
from rest_framework.exceptions import APIException


class IsClientManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST', 'PUT')
        SUPPORT_GRANTED_METHOD = ('GET')

        try:
            user = User.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if user.groups.filter(name='MANAGER').exists():

                if request.user.is_authenticated:
                    return True

            if user.groups.filter(name='SALES').exists():

                if (
                    request.user.is_authenticated
                    and request.method in SALES_GRANTED_METHOD
                ):
                    return True

            if user.groups.filter(name='SUPPORT').exists():
                if (
                    request.user.is_authenticated
                    and request.method in SUPPORT_GRANTED_METHOD
                ):
                    return True

            return False

        except User.DoesNotExist:
            raise APIException('You are not allowed.')


class IsContractManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST', 'PUT')
        SUPPORT_GRANTED_METHOD = ('GET')

        try:
            user = User.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if user.groups.filter(name='MANAGER').exists():

                if request.user.is_authenticated:
                    return True

            if user.groups.filter(name='SALES').exists():

                if (
                    request.user.is_authenticated
                    and request.method in SALES_GRANTED_METHOD
                ):
                    return True

            if user.groups.filter(name='SUPPORT').exists():
                if (
                    request.user.is_authenticated
                    and request.method in SUPPORT_GRANTED_METHOD
                ):
                    return True

            return False

        except User.DoesNotExist:
            raise APIException('You are not allowed.')


class IsEventManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST', 'PUT')
        SUPPORT_GRANTED_METHOD = ('GET', 'PUT')

        try:
            user = User.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if user.groups.filter(name='MANAGER').exists():

                if request.user.is_authenticated:
                    return True

            if user.groups.filter(name='SALES').exists():

                if (
                    request.user.is_authenticated
                    and request.method in SALES_GRANTED_METHOD
                ):
                    return True

            if user.groups.filter(name='SUPPORT').exists():
                if (
                    request.user.is_authenticated
                    and request.method in SUPPORT_GRANTED_METHOD
                ):
                    return True

            return False

        except User.DoesNotExist:
            raise APIException('You are not allowed.')
