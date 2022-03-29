# from django.test import TestCase
from testing.testscases import TestCase
from recyclebin.RecyclebinServer import RecyclebinServer


# Create your tests here.

class recyclebinTest(TestCase):
    def test_minute_to_now(self):
        ruize, _ = self.create_user_client('ruize')
        path = ruize.profile.source_path
        file1 = self.create_source_file(path, 'file1')
        garbage = self.create_garbage(file1)
        print(RecyclebinServer.get_rest_minute(garbage))
