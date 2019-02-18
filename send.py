import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTUwNTE4OTgwLCJqdGkiOiI4NDI5MTE2ZGQ5OGM0ZjdmOGFlZjg0OGEyODZiYzY1OCIsInVzZXJfaWQiOjF9.q7z1k-lC7xy1HOCBFhsVAbmcSE8G-vkV-vwKR8rjhHA'
r = requests.get('http://127.0.0.1:8000/languages', headers=headers)

print(r.text)


# https://jwt.io/
