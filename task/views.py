from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from task.serializers import ToDoSerializer
from task.models import ToDo
from task.permissions import ToDoPermission


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    permission_classes = (IsAuthenticated, ToDoPermission)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status', 'priority')

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            self.queryset = self.queryset.filter(user_id=request.user.id)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
