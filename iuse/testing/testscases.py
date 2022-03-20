from django.test import TestCase as django_TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class TestCase(django_TestCase):
    @property
    def anonymous_client(self):
        if hasattr(self, "_anonymous_client"):
            return self._anonymous_client
        self._anonymous_client = APIClient()
        return self._anonymous_client
    def create_user_client(self, username, password=None, email=None):
        if password is None:
            password = 'correct password'
        if email is None:
            email = f'{username}@qq.com'
        user =  User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        client = APIClient()
        client.force_authenticate(user)
        return user, client