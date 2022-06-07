from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated or request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
