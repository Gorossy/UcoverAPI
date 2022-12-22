from rest_framework.permissions import BasePermission

class IsCoverer(BasePermission):
    def has_permission(self, request, view):
        # Solo los usuarios con el rol "coverer" tienen permiso para acceder a la vista
        return request.user and (request.user.role == 'coverer' or request.user.role == 'admin')
class isClient(BasePermission):
    def has_permission(self, request, view):
        # Solo los usuarios con el rol "client" tienen permiso para acceder a la vista
        return request.user and (request.user.role == 'client' or request.user.role == 'admin')