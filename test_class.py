import unittest
from flask import jsonify
from manage import app

class Test(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.app.post('/user/', data=jsonify({'login': 'test@mail.ru', 'password': 'test12345', 'name': 'test'}))
        self.assertEqual(response.status_code, 200)

    def test_authentication(self):
        response = self.app.post('/auth/', data=jsonify({'login':'test@mail.ru', 'password':'test12345'}))
        self.assertEqual(response.status_code, 200)