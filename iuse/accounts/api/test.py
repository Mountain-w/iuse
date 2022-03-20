from testing.testscases import TestCase
from rest_framework.test import APIClient
LOGIN_URL = '/api/accounts/login/'
LOGOUT_URL = '/api/accounts/logout/'
SIGNUP_URL = '/api/accounts/signup/'
LOGIN_STATUS = '/api/accounts/login_status/'

class AccountTest(TestCase):
    def setUp(self):
        self.ruize, self.ruize_client = self.create_user_client('ruize')

    def test_login(self):
        data = {}

        # 测试用户不存在
        data['username'] = 'wrongname'
        data['password'] = 'correct password'
        response = self.anonymous_client.post(LOGIN_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试密码错误
        data['username'] = self.ruize.username
        data['password'] = 'wrongpassword'
        response = self.anonymous_client.post(LOGIN_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试 get 方法无效
        response = self.anonymous_client.get(LOGIN_URL, data)
        self.assertEqual(response.status_code, 405)

        # 测试正常登录
        data['username'] = self.ruize.username
        data['password'] = 'correct password'
        client = APIClient()
        response = client.post(LOGIN_URL, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['id'], self.ruize.id)


    def test_logout(self):
        # 测试get方法无效
        response = self.ruize_client.get(LOGOUT_URL)
        self.assertEqual(response.status_code, 405)

        # 测试未登录登出
        client = APIClient()
        response = client.post(LOGOUT_URL)
        self.assertEqual(response.status_code, 200)

        # 测试正常登出
        # 先登录
        data = {}
        data['username'] = self.ruize.username
        data['password'] = 'correct password'
        client = APIClient()
        client.post(LOGIN_URL, data)
        response = client.post(LOGOUT_URL)
        self.assertEqual(response.status_code, 200)
        response = client.get(LOGIN_STATUS)
        self.assertEqual(response.data['has_logged_in'], False)

    def test_signup(self):
        data = {}
        # 测试get方法失效
        data['username'] = 'wrongname'
        data['password'] = 'password'
        data['email'] = 'ruize01@qq.com'
        response = self.anonymous_client.get(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 405)

        # 测试名字太长
        data['username'] = 'tolonglonglonglonglonglonglonglonglonglong'
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试名字太短
        data['username'] = 'to'
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试密码太长
        data['username'] = 'ruize01'
        data['password'] = 'tooooooooooooooooooooooooolong'
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试密码太短
        data['username'] = 'ruize01'
        data['password'] = 't'
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试邮箱格式不合格
        data['username'] = 'ruize01'
        data['password'] = 'correctpassword'
        data['email'] = 'ruizehandsome'
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 测试邮箱被注册
        data['username'] = 'ruize01'
        data['password'] = 'correctpassword'
        data['email'] = self.ruize.email
        response = self.anonymous_client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 400)

        # 正常注册
        data['username'] = 'ruize01'
        data['password'] = 'correctpassword'
        data['email'] = 'ruize01@qq.com'
        client = APIClient()
        response = client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 201)
        response = client.get(LOGIN_STATUS)
        self.assertEqual(response.data['has_logged_in'], True)
        self.assertEqual(response.data['user']['username'], data['username'])

