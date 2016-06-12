# from rest_framework.decorators import detail_route, list_route
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import viewsets

from .models import User
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    '''    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ListUserSerializer
        elif self.request.method == 'POST':
            return serializers.CreateUserSerializer
        else:
            return serializers.UpdateUserSerializer'''

    def perform_destroy(self, user):
        """
        Unselect `is_active` instead of deleting accounts.
        """
        user.is_active = False
        user.save()
