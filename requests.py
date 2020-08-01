import requests


r = requests.post('https://127.0.0.1:5000/user/', data = {'login':'test', 'password':'123'})