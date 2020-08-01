import unittest
from manage import app

class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_requests(self):
        response = self.app.post('http://127.0.0.1:5000/auth/', data = {'login':'test', 'password':'123'})
        self.assertEqual(response.status_code, 200)