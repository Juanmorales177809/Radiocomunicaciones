# from gmplot import *
import folium

# API_KEY= "AIzaSyCFsu2GOmmIlGITm0gHOP6P1xRoMZBGBlw"


# map= gmplot.GoogleMapPlotter(6.2800171 ,-75.4426875,13,apikey=API_KEY)
# map.draw('./gradel/mapa.html')

def create(coor,coor1,text, text1):
    res = [float(idx) for idx in coor.split(',')]
    res1 = [float(idx) for idx in coor1.split(',')]
    mapa= folium.Map(location=(res),zoom_start=12,control_scale=True)
    folium.Marker((res), popup='Punto UNO',tooltip=text).add_to(mapa)
    folium.Marker((res1),popup='Punto DOS', tooltip= text1).add_to(mapa)
    mapa.save('./gradel/mapa_prueba.html')

