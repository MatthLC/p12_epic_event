from rest_framework.permissions import BasePermission
from authentication.models import User


class IsManager(BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if user.groups.filter(name='MANAGER').exists():

                if request.user.is_authenticated:
                    return True

            return False

        except User.DoesNotExist:
            return 'Pas de correspondance'
