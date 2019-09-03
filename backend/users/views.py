from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer
