import requests
import re


def get_rext_request(url):
    try:
        request = requests.get(url)
        return request.text
    except:
        return ''


expression = r'[\w\.-_]+@+[\w-_]+\.+[\w-_]'
url = 'https://www.lacosdefilo.com/'

text_web_site = get_rext_request(url)
expression = re.findall(r'[\w\.\_-]+@+[\w\_-]+\.+[\w\_-]+', text_web_site)

if expression:
    print(expression)
else:
    print('Email não encontrado no site!')