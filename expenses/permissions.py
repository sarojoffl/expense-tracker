from rest_framework import permissions


class IsOwnerOrSuperuser(permissions.BasePermission):
    """Allows access to owner or superuser."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser
