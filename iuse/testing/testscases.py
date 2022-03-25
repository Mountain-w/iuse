from django.test import TestCase as django_TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from utils.auth.authhelper import generate_token
from sources.models import Source
from utils.modelshelpers.enums import FileType
from sources.SourceServer import SourceServer
import os
from iuse.settings import TEST_BASE_DIR

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
        SourceServer.create_sources_for_test(user.profile.source_path)
        return user, client

    def create_source_dir(self, parent, name):
        return Source.objects.create(parent_dir_id=parent.id, name=name, type=FileType.DIR, owner=parent.owner)

    def create_source_file(self, parent, name):
        return Source.objects.create(parent_dir_id=parent.id, name=name, type=FileType.FILE, owner=parent.owner)

    def exists(self, source):
        path = SourceServer.generate_path(source)
        path = os.path.join(TEST_BASE_DIR, path)
        return os.path.exists(path)