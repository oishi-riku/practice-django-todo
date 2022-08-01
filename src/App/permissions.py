from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, req, view, obj):
        if req.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == req.user