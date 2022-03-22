from django.utils.deprecation import MiddlewareMixin
# from rest_framework.response import Response
from django.http.response import JsonResponse as Response
from utils.exceptions.exceptions import TokenInvalid, TokenOutDate

from utils.auth.authhelper import checkout_token, get_user

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_view(self, request, func, *args, **kwargs):
        auth_head = request.META.get('HTTP_AUTHORIZATION')
        action = request.path.split('/')
        if action[-2] != 'login':
            if not auth_head:
                return Response({"error": "You don't have the Authorization"})
            else:
                auth_head = auth_head
                try:
                    checkout_token(auth_head)
                except TokenInvalid:
                    return Response({"error": "You token is valid", "error_code":4000})
                except TokenOutDate:
                    return Response({"error": "Your token is OutDate", "error_code":3000})
                else:
                    user = get_user(auth_head)
                    request.user = user

