import requests
import json
import time
import os

urlAPI = 'http://data.fixer.io/api/'
functionAPI = 'latest'
keyAPI = {'access_key': 'a2b8a8bef4afe16011dfc7a74976b848'}
baseAPI = {'base': 'BRL'}
timeForSleep = 5
clear = lambda : os.system('cls')

keysAPI = {
    'success': 'success',
    'block': 'rates',
    'valueBRL': 'BRL',
    'valueUSD': 'USD'
}

def consumerAPI(url):
    result = None

    try:
        request = requests.get(url)
        resultJSON = json.loads(request.text)

        if resultJSON[keysAPI['success']]:
            result = resultJSON
    except:
        print("API Consumer error!")

    return result


def encodeURL(url, function, args):
    result = str(url)
    result += function

    args = dict(args)
    for key, value in args.items():
        result += ''.join(['&', key, '=', value])

    return result


def printLoading():
    clear()
    print('|-------------------------------------')
    print('|Refrash, Loading...')
    print('|-------------------------------------')


def printQuotation(valueBRL, valueUSD):
    valueB = float(valueBRL)
    valueU = float(valueUSD)

    value = valueB - valueU

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
        printLoading()
        parameters = {}
        parameters.update(keyAPI)
        #API free version does not support changing base
        #parameters.update(baseAPI)
        urlAPIEncode = encodeURL(urlAPI, functionAPI, parameters)
        jsonResponse = consumerAPI(urlAPIEncode)
        jsonBlok = jsonResponse[keysAPI['block']]
        printQuotation(jsonBlok[keysAPI['valueBRL']], jsonBlok[keysAPI['valueUSD']])
        time.sleep(timeForSleep)


main()