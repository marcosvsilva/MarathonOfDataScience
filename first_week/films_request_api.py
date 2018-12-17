import requests
import json
import shutil
import tkinter
from PIL import ImageTk, Image

'''
TODO: refactor using regular expression
'''
listDecodeString = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
                    '}', '~')

listEncodeString = ('21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F'
                    '3A', '3B', '3C', '3D', '3E', '3F', '40', '5B', '5C', '5D', '5E', '5F', '60', '7B', '7C',
                    '7D', '7E')


def decodeString(arg):
    result = str(arg)

    for chr in str(arg):
        if chr in listDecodeString:
            position = listDecodeString.index(chr)
            result = result.replace(chr, ''.join(['#', listEncodeString[position]]))

    result = result.replace(' ', '+')

    return result


def mountRequest(url_request, args):
    args = dict(args)
    url_request = str(url_request)
    key, value = args.popitem()

    url_request += '?'
    url_request += key + '=' + value

    for key, value in args.items():
        url_request += '&' + key + '=' + decodeString(value)

    return url_request


def printDetails(film):
    if film['Response'].upper() == 'True'.upper():
        print('Title: ' + film['Title'])
        print('Year: ' + film['Year'])
        print('Rated: ' + film['Rated'])
        print('Released: ' + film['Released'])
        print('Runtime: ' + film['Runtime'])
        print('Genre: ' + film['Genre'])
        print('Director: ' + film['Director'])
        print('Writer: ' + film['Writer'])
        print('Actors: ' + film['Actors'])
        print('Plot: ' + film['Plot'])
        print('Language: ' + film['Language'])
        print('Country: ' + film['Country'])
        print('Awards: ' + film['Awards'])
    else:
        print('Movie not found!')


def printPosterFilm(link):
    if link != '':
        if downloadImage(link):
            try:
                showImage('poster.png')
            except:
                print('Error print poster!')


def showImage(nameImage):
    imageWindow = tkinter.Tk()
    img = ImageTk.PhotoImage(Image.open(nameImage))
    panel = tkinter.Label(imageWindow, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    imageWindow.mainloop()


def downloadImage(link):
    try:
        request = requests.get(link, stream=True)
        with open('poster.png', 'wb') as imageOut:
            shutil.copyfileobj(request.raw, imageOut)
        del request
        return True
    except:
        print('Error print film poster!')
        return False


def consummerAPI(urlRequest):
    try:
        request = requests.get(urlRequest)
        resultJSON = json.loads(request.text)
        return resultJSON
    except:
        print('Error connection!')
        return None


url_request = 'http://www.omdbapi.com/'
args = {}

##Title
title = str(input('Enter film title:'))
if title != '':
    args.update({'t': title})

##Year
year = str(input('Enter year film:'))
try:
    if year != '':
        if int(year) > 0:
            args.update({'y':year})
except:
    print('Invalid year!')

##Api Key
args.update({'apikey': '56e8adf3'})

resumeFilm = consummerAPI(mountRequest(url_request, args))
if resumeFilm != None:
    printDetails(resumeFilm)
    printPosterFilm(resumeFilm['Poster'])