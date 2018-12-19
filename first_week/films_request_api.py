import requests
import json
import shutil
import tkinter
import urllib.parse
from PIL import ImageTk, Image


def mount_request(url, parameters):
    parameters = dict(parameters)
    url = str(url)
    key, value = parameters.popitem()

    url += '?'
    url += key + '=' + value

    for key, value in parameters.items():
        url += '&' + key + '=' + urllib.parse.quote_plus(value)

    return url


def print_details(film):
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


def print_poster_film(link):
    if link != '':
        if download_image(link):
            try:
                show_image('poster.png')
            except:
                print('Error print poster!')


def show_image(name_image):
    image_window = tkinter.Tk()
    photo_image = ImageTk.PhotoImage(Image.open(name_image))
    panel = tkinter.Label(image_window, image=photo_image)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()


def download_image(link):
    try:
        request = requests.get(link, stream=True)
        with open('poster.png', 'wb') as image_out:
            shutil.copyfileobj(request.raw, image_out)
        del request
        return True
    except:
        print('Error print film poster!')
        return False


def consummer_api(url_request):
    try:
        request = requests.get(url_request)
        result_json = json.loads(request.text)
        return result_json
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

resume_film = consummer_api(mount_request(url_request, args))
if resume_film != None:
    print_details(resume_film)
    print_poster_film(resume_film['Poster'])