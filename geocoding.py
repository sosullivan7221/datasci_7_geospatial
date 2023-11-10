import os
from dotenv import load_dotenv
import requests 
import urllib.parse
import json
import pandas as pd

load_dotenv()

APIKEY = os.getenv("APIKEY")

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/3ccdc2b145a6cc291ca8f4cf45486575d3d97886/WK7/assignment7_slim_hospital_addresses.csv')
df['NewAddress'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']
df_sample = df['NewAddress'].sample(n=100)
google_response = []

for address in df_sample: 
    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + APIKEY
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df_final = pd.DataFrame(google_response)
df_final.to_csv('geocoding.csv')