from django.core.files.uploadedfile import SimpleUploadedFile

from testing.testscases import TestCase

SOURCES_API = '/api/sources/{}/'
CREATE_API = '/api/sources/{}/create_dir/'
UPLOAD_API = '/api/sources/{}/upload/'


class SourceApiTest(TestCase):
    # def test_retrieve(self):
    #     # 创建用户
    #     user1, user1_client = self.create_user_client('user1')
    #     dir1 = self.create_source_dir(user1.profile.source_path, 'dir1')
    #     dir2 = self.create_source_dir(user1.profile.source_path, 'dir2')
    #     dir3 = self.create_source_dir(user1.profile.source_path, 'dir3')
    #     file1 = self.create_source_file(user1.profile.source_path, 'file1')
    #     # 未登录不可访问
    #     response = self.anonymous_client.get(SOURCES_API.format(user1.profile.source_path.id))
    #     self.assertEqual(response.status_code, 403)
    #     # post 方法无效
    #     response = user1_client.post(SOURCES_API.format(user1.profile.source_path.id))
    #     self.assertEqual(response.status_code, 405)
    #     # 正常访问文件夹
    #     response = user1_client.get(SOURCES_API.format(user1.profile.source_path.id))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data['children']), 4)
    #     self.assertEqual(response.data['id'], user1.profile.source_path.id)
    #     self.assertEqual(response.data['children'][0]['id'], dir1.id)
    #     # 正常访问文件
    #     response = user1_client.get(SOURCES_API.format(file1.id))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['name'], file1.name)

    # def test_create_dir(self):
    #     # 创建用户
    #     ruize01, ruize01_client = self.create_user_client('ruize01')
    #     path = ruize01.profile.source_path
    #     # 创建文件夹
    #     data = {
    #         'name': 'Movies'
    #     }
    #     response = ruize01_client.post(CREATE_API.format(path.id), data)
    #     self.assertEqual(response.status_code, 201)
    #     response = ruize01_client.get(SOURCES_API.format(path.id))
    #     self.assertEqual(response.data["children"][0]['name'], 'Movies')

    def test_upload_file(self):
        # 创建用户
        ruize02, ruize02_client = self.create_user_client('ruize02')
        path = ruize02.profile.source_path
        file = SimpleUploadedFile(
            name='1.txt',
            content=str.encode('别出bug'),
            content_type="text/plain"
        )
        response = ruize02_client.post(UPLOAD_API.format(path.id), {
            'file': file
        })
        print(response.data)