import oauth2 as oauth
import json
import pprint
import urllib.parse

key = ''
key_secret = ''

token = ''
token_secret = ''

consumer = oauth.Consumer(key, key_secret)
token = oauth.Token(token, token_secret)
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