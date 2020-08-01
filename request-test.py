import requests


r = requests.post('http://127.0.0.1:5000/auth/', data = {'login':'test', 'password':'123'})
r = requests.get('http://127.0.0.1:5000/')
print('Ok')