from rest_framework.permissions import BasePermission
from datetime import date
class Permission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False

class Days(BasePermission):
	def has_object_permission(self, request, view, obj):
            days=(obj.date - date.today()).days
            if (days > 3):
                return True
            else:
                return False
