import oauth2 as oauth
import json
import pprint
import urllib.parse

keyAPI = ''
keySecretAPI = ''

keyTokenAPI = ''
keyTokenSecretAPI = ''

consumer = oauth.Consumer(keyAPI, keySecretAPI)
token = oauth.Token(keyTokenAPI, keyTokenSecretAPI)
client = oauth.Client(consumer, token)

search = str(input('Pesquisa: '))
search = urllib.parse.quote(search, safe='')

request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + search)
json = json.loads(request[1].decode())
twitts = json['statuses']


for twit in twitts:
    pprint.pprint(twit['user']['screen_name'])
    pprint.pprint(twit['text'])
    print()