import requests
import re


def getTextRequest(url):
    try:
        request = requests.get(url)
        return request.text
    except:
        return ''


expression = r'[\w\.-_]+@+[\w-_]+\.+[\w-_]'
url = 'https://www.lacosdefilo.com/'

textWebSite = getTextRequest(url)
expression = re.findall(r'[\w\.\_-]+@+[\w\_-]+\.+[\w\_-]+', textWebSite)

if expression:
    print(expression)
else:
    print('Email não encontrado no site!')