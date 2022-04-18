import requests
import time

API_KEY= "AIzaSyDZTB5K_IEWmVO1XH_22HSSlPh-0vixuvU"
address= '6.2825086'

params = {
    'key': API_KEY,
    'address': address
}

base_url= 'https://maps.googleapis.com/maps/api/geocode/json?'
response= requests.get(base_url,params=params).json()
response.keys()

def revisar():
    lista= list(response.items())
    lista= lista[0][1][0]
    lista= list(lista.items())
    lista= lista[2]
    lista= lista[1]
    k= lista.keys()
    print(lista.get('location'))



if response['status']=='OK':
    geometry= response['results'][0]['geometry']

if __name__=="__main__":
    revisar()

