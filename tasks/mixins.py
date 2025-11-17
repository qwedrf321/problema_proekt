from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin:
    """
    Mixin to ensure that the logged-in user is the owner of the object.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied("You do not have permission to access this object.")
        return super().dispatch(request, *args, **kwargs)