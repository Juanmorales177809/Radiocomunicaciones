# from gmplot import *
import folium

# API_KEY= "AIzaSyCFsu2GOmmIlGITm0gHOP6P1xRoMZBGBlw"


# map= gmplot.GoogleMapPlotter(6.2800171 ,-75.4426875,13,apikey=API_KEY)
# map.draw('./gradel/mapa.html')

def create(coor):
    res = [float(idx) for idx in coor.split(',')]
    mapa= folium.Map(location=(res))
    mapa.save('./gradel/mapa_prueba.html')

