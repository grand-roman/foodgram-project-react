from rest_framework import permissions


class AuthPostRetrieve(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS 
                or super().has_permission(request, view))



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS 
                or obj.author == request.user)
