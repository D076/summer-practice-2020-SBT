import json
import unittest
from manage import app

class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestLoader.sortTestMethodsUsing = None
        app.testing = True
        self.app = app.test_client()
        self.token = ''

    def tearDown(self):
        pass

    def test_0_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_1_registration(self):
        info = {'login': 'test@mail.ru', 'password': 'test12345', 'name': 'test'}
        response = self.app.post('/user/', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_2_authentication(self):
        info = {'login':'test@mail.ru', 'password':'test12345'}
        response = self.app.post('/auth/', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        
        #    
        # тестовый блок
        # 

        # json_response = response.json()
        # self.token = json_response['token']
        self.assertEqual(self.token, '111111')

        # 
        # конец
        # 

        # self.token = str(response.data)
        self.assertEqual(response.status_code, 200)

    def test_3_validation(self):
        info = self.token
        response = self.app.get('/validate/{info}/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # def test_4_logout(self):
    #     info = self.token
    #     response = self.app.get('/logout/{info}/', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)
    
    # def test_5_validation(self):
    #     info = self.token
    #     response = self.app.get('/validate/{info}/', follow_redirects=True)
    #     self.assertEqual(response.status_code, 404)