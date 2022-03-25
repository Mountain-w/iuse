from rest_framework.permissions import BasePermission


class IsSourceOwner(BasePermission):
    message = "Your aren't the Source's owner, you can't modify it"

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
