from multiprocessing.connection import Client
from re import A
from matplotlib.pyplot import draw, scatter
import requests
import time
import googlemaps
from gmplot import *
from datetime import datetime



API_KEY= "AIzaSyCFsu2GOmmIlGITm0gHOP6P1xRoMZBGBlw"
map= gmplot.GoogleMapPlotter(6.2800171 ,-75.4426875,13,apikey=API_KEY)
map.draw('./gradel/mapas.html')

# address= '6.2825086'
# Client
# params = {
#     'key': API_KEY,
#     'address': address
# }

# base_url= 'https://maps.googleapis.com/maps/api/geocode/json?'
# response= requests.get(base_url,params=params).json()
# response.keys()
# gmaps= googlemaps.Client(key=API_KEY)
#
# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Santa de de antioquia",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
                                     

# def revisar():
#     lista= list(response.items())
#     lista= lista[0][1][0]
#     lista= list(lista.items())
#     lista= lista[2]
#     lista= lista[1]
#     k= lista.keys()
#     print(lista.get('location'))

#map.geocode(map,'medellin',apikey=API_KEY)#centrar mapa
#map.geocoder.elevation(map,address)
# if response['status']=='OK':
#     geometry= response['results'][0]['geometry']

if __name__=="__main__":
    pass

