from rest_framework import permissions


class ToDeleteUser(permissions.BasePermission):
    """
    Permission for deleting user.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
