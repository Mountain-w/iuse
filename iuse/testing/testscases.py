from django.test import TestCase as django_TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from utils.auth.authhelper import generate_token
from sources.models import Source
from utils.modelshelpers.enums import FileType

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
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        client = APIClient()
        token = generate_token(user.username)
        client.credentials(HTTP_AUTHORIZATION=token)
        user.profile
        return user, client

    def create_source_dir(self, parent_id, name):
        return Source.objects.create(parent_dir_id=parent_id, name=name, type=FileType.DIR)

    def create_source_file(self, parent_id, name):
        return Source.objects.create(parent_dir_id=parent_id, name=name, type=FileType.FILE)