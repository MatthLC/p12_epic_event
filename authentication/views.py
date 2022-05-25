from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import UserSerializer, UserListSerializer
from authentication.models import User

from authentication.permissions import IsManager


"""
access link : /signup/
"""


class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return


"""
Display user list registered
access link : /userlist/
"""


class UserListViewset(ReadOnlyModelViewSet):

    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
