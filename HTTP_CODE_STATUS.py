import requests

x = requests.get('https://www.google.com.br')
status = x.status_code

print(x.status_code)

