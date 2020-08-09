import json
import unittest
from manage import app


class Test(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()


    def tearDown(self):
        pass


    def test_0_index(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_1_registration(self):
        info = {'login': 'test@mail.ru', 'password': 'test12345', 'name': 'test'}
        response = self.app.post('/user', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)


    def test_2_auth_valid_logout(self):
        info = {'login':'test@mail.ru', 'password':'test12345'}

        # Auth test
        response_auth = self.app.post('/auth', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response_auth.status_code, 200)

        token = response_auth.data.decode('utf8')

        # Validation test
        response_valid = self.app.get(f'/validate/{token}', follow_redirects=True)
        self.assertEqual(response_valid.status_code, 200)

        # Logout test
        response_logout = self.app.get(f'/logout/{token}', follow_redirects=True)
        self.assertEqual(response_logout.status_code, 200)

        # Validation test
        response_valid = self.app.get(f'/validate/{token}', follow_redirects=True)
        self.assertEqual(response_valid.status_code, 404)


    def test_3_user_info_by_token(self):
        info = {'login':'test@mail.ru', 'password':'test12345'}

        # Auth test
        response_auth = self.app.post('/auth', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response_auth.status_code, 200)

        token = response_auth.data.decode('utf8')

        # User info by token test
        response_user_info = self.app.get(f'/user/info/{token}', follow_redirects=True)
        self.assertEqual(response_user_info.status_code, 200)

        user_info = json.loads(response_user_info.data.decode('utf8'))
        self.assertEqual(user_info['login'], 'test@mail.ru')
        self.assertEqual(user_info['name'], 'test')


    def test_4_user_info_by_login(self):
        # User info by login test
        response_user_info = self.app.get('/user/info/public/test@mail.ru', follow_redirects=True)
        self.assertEqual(response_user_info.status_code, 200)

        user_info = json.loads(response_user_info.data.decode('utf8'))
        self.assertEqual(user_info['login'], 'test@mail.ru')
        self.assertEqual(user_info['name'], 'test')
