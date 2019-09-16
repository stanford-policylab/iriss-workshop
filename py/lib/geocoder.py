import csv
import requests

CENSUS_GEO_HOST = 'https://geocoding.geo.census.gov/geocoder/locations'
ONELINE_ENDPT = '/onelineaddress'
STRUCT_ENDPT = '/address'

def census_geocode_structured(address):
    params = {
        'benchmark': 'Public_AR_Current',
        'format': 'json',
    }
    params.update(address)
    response = requests.get(CENSUS_GEO_HOST + STRUCT_ENDPT, params=params)
    coords = response.json()['result']['addressMatches'][0]['coordinates']
    return {'lat': coords['y'], 'lng': coords['x']}

def census_geocode_csv(input_csv):
    addresses = []
    with open(input_csv) as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            addresses.append({headers[i]: v for i, v in enumerate(row)})
    return [census_geocode_structured(address) for address in addresses]
