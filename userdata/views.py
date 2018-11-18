from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from django.contrib.auth import get_user_model

from userdata.serializers import UserSerializer
from userdata.permissions import ToDeleteUser


User = get_user_model()


class UserViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = (ToDeleteUser, )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
