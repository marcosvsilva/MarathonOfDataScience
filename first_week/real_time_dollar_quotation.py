import requests
import json
import time
import os

url_api = 'http://data.fixer.io/api/'
function_api = 'latest'
key_api = {'access_key': 'a2b8a8bef4afe16011dfc7a74976b848'}
base_api = {'base': 'BRL'}
time_sleep = 5

keys_api = {
    'success': 'success',
    'block': 'rates',
    'valueBRL': 'BRL',
    'valueUSD': 'USD'
}


def clear():
    os.system('cls')


def consumer_api(url):
    result = None

    try:
        request = requests.get(url)
        result_json = json.loads(request.text)

        if result_json[keys_api['success']]:
            result = result_json
    except:
        print("API Consumer error!")

    return result


def encode_url(url, function, args):
    result = str(url)
    result += function

    args = dict(args)
    for key, value in args.items():
        result += ''.join(['&', key, '=', value])

    return result


def print_loading():
    clear()
    print('|-------------------------------------')
    print('|Refrash, Loading...')
    print('|-------------------------------------')


def print_quotation(brl, usd):
    value_brl = float(brl)
    value_usd = float(usd)

    value = value_brl - value_usd

    clear()
    print('|-------------------------------------')
    print('|')
    print('|Dollar Value: %.6f' % value)
    print('|')
    print('|refreshing in 5 seconds')
    print('|')
    print('|-------------------------------------')


def main():
    while True:
        print_loading()
        parameters = {}
        parameters.update(key_api)
        #API free version does not support changing base
        #parameters.update(baseAPI)
        url_api_encode = encode_url(url_api, function_api, parameters)
        json_response = consumer_api(url_api_encode)
        json_blok = json_response[keys_api['block']]
        print_quotation(json_blok[keys_api['valueBRL']], json_blok[keys_api['valueUSD']])
        time.sleep(time_sleep)


main()