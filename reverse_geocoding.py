import os
from dotenv import load_dotenv
import requests 
import urllib.parse
import json
import pandas as pd

load_dotenv()

APIKEY = os.getenv("APIKEY")

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/3ccdc2b145a6cc291ca8f4cf45486575d3d97886/WK7/assignment7_slim_hospital_coordinates.csv')
df['NewCoordinates'] = df['X'].astype('str') + ',' + df['Y'].astype('str')
df_sample = df['NewCoordinates'].sample(n=100)

google_response = []

for coordinates in df_sample:

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = coordinates

    url_request_part1 = search + location_raw + '&key=' + APIKEY
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    address = response_dictionary['results'][0]['formatted_address']
    
    final = {'coordinates': coordinates, 'address': address}
    google_response.append(final)

    print(f'....finished with {coordinates}')


df_final = pd.DataFrame(google_response)
df_final.to_csv('reverse_geocoding.csv')
