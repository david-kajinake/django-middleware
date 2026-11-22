from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils import timezone

class IpBlacklistMiddleware:
    """
    This middleware checks if the Ip address of the incoming / outgoing request is found in a list
    BANNED_IPS and blocks it right away if the condition is True
    """
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        if hasattr(settings, 'BANNED_IPS') and settings.BANNED_IPS is not None:
            if request.META['REMOTE_ADDR'] in settings.BANNED_IPS:
                raise PermissionDenied
        response= self.get_response(request)
        return response


class UserLastSeenMiddleware:
    """
    This middleware updates the user's last seen anytime the user makes a request.
    """
    def __init__(self, get_response):
        self.get_response= get_response

    def __call__(self, request):
        user= request.user
        if user.is_authenticated and user.last_seen:    
            user.last_seen= timezone.datetime.now()
            user.save()
        response= self.get_response(request)
        return response