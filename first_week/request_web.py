import requests

request_get = requests.get('https://putsreq.com/115oCs3lFEzPa4EoleUv')
request_post = requests.post('https://putsreq.com/115oCs3lFEzPa4EoleUv')

print(request_get.text)
print(request_post.text)