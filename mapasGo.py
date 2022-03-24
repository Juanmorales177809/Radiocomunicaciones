import requests

API_KEY= "AIzaSyDZTB5K_IEWmVO1XH_22HSSlPh-0vixuvU"
address= '1 hack drive, menlo park, CA'

params = {
    'key': API_KEY,
    'address': address
}

base_url= 'https://maps.googleapis.com/maps/api/geocode/json?'
response= requests.get(base_url,params=params).json()
response.keys()

if response['status']=='OK':
    geometry= response['results'][0]['geometry']

print(response)