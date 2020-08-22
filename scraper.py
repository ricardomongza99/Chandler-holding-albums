from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import json
from time import sleep
from random import randint

def get_name(text):
    # remove extra spaces
    name = re.sub(' +', ' ', text[1])
    # remove beginning space
    return name[1:]

def get_band(text):
    band = re.sub(' +', ' ', text[2])
    return band[3:]

def get_year(text):
    # show only
    return text[-4:]
#---------------------------------------------------------

site = "https://www.metacritic.com/browse/albums/score/metascore/all/filtered?view=detailed&page=0"
hdr = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(site, headers=hdr)
soup = BeautifulSoup(r.text, 'html.parser')

album_containers = soup.find_all('tr')

print(len(album_containers))

names = []
bands = []
years = []
ratings = []

albums = {}
albums['album'] = []

pages = [str(i) for i in range(0,4)]


for container in album_containers:
    # check if its possible to extract
    if container.h3 is not None:

        names_text = container.h3.text.split('\n')
        date_text = container.find_all('div', {'class': 'clamp-details'})[1].text[:-1]
        rating_text = container.find_all('div', {'class': 'metascore_w large release positive'})[0].text

        name = get_name(names_text).replace('/', ' ')
        band = get_band(names_text)
        year = int(get_year(date_text))
        rating = int(rating_text)
        image = (name + '.jpg')

        names.append(name)
        bands.append(band)
        years.append(year)
        ratings.append(rating)

        image_url = container.img['src']
        #urllib.request.urlretrieve(image_url, (f"album_covers/{image}"))

        #JSON
        albums['album'].append({
            'name': name,
            'band': band,
            'year': year,
            'rating': rating,
            'image': image
        })

for i, name in enumerate(names):
    print(i, name)

with open("albums.json", 'w') as outfile:
    json.dump(albums, outfile, indent=2)
