from rest_framework import permissions


class ToDoPermission(permissions.BasePermission):
    """
    Permission for ToDo.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.user_id== request.user.id
