import requests

def mountRequest(url_request, args):
    args = dict(args)
    url_request = str(url_request)
    key, value = args.popitem()

    url_request += '?'
    url_request += key + '=' + value

    for key, value in args.items():
        url_request += '&' + key + '=' + value

    return url_request

url_request = 'http://www.omdbapi.com/'
args = {}

##Title
title = str(input('Enter film title:'))
args.update({'t': title})


args.update({'apikey': '56e8adf3'})
url_request = mountRequest(url_request, args)

request = requests.get(url_request)
print(request.text)