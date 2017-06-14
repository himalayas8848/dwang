import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, name,elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=nm+": "+str(el)))

map.add_child(fgv)

#fgp = folium.FeatureGroup(name="Population")

#fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
#style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
#else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'white'}))

#map.add_child(fgp)
#map.add_child(folium.LayerControl())

map.save("Map1.html")
