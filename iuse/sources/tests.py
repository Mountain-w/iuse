# from django.test import TestCase
# Create your tests here.
from testing.testscases import TestCase
from sources.SourceServer import SourceServer


class SourceModelTest(TestCase):
    def test_generate_path(self):
        ruize, ruize_client = self.create_user_client('ruize')
        dir1 = self.create_source_dir(ruize.profile.source_path.id, 'dir1')
        dir2 = self.create_source_dir(dir1.id, 'dir2')
        dir3 = self.create_source_dir(dir2.id, 'dir3')
        dir4 = self.create_source_dir(dir3.id, 'dir4')
        file1 = self.create_source_file(dir4.id, 'file.py')
        path = SourceServer.generate_path(file1)
        self.assertEqual(path, 'ruize/dir1/dir2/dir3/dir4/file.py')
