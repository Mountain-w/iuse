from django.utils.deprecation import MiddlewareMixin
# from rest_framework.response import Response
from django.http.response import JsonResponse as Response
from utils.exceptions.exceptions import TokenInvalid, TokenOutDate
from rest_framework import status
from utils.auth.authhelper import checkout_token, get_user


def check_token(auth_head=None):
    if not auth_head:
        return None
    auth_head = auth_head
    try:
        checkout_token(auth_head)
    except TokenInvalid:
        return Response({"error": "You token is valid", "error_code": 4000}, status=401)
    except TokenOutDate:
        return Response({"error": "Your token is OutDate", "error_code": 3000}, status=401)
    else:
        user = get_user(auth_head)
    return user


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_view(self, request, func, *args, **kwargs):
        auth_head = request.META.get('HTTP_AUTHORIZATION')

        if auth_head:
            request.user = check_token(auth_head)