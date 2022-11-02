from rest_framework import permissions

# Class that checks if the requesting user is the owner to grant access to modify the post or not:
class IsOwnerOrReadOnly(permissions.BasePermission):
    # Method that checks if the requesting user is the owner of the given post:
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.owner == request.user