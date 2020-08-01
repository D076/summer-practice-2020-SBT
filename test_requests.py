import requests


r = requests.post('127.0.0.1:5000/user/', data = {'login':'test', 'password':'123'})
print('Ok')