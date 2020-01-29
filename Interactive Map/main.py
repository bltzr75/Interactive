import folium
import pandas

#Create Data Frame object
data=pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Function to dynamically change the popup colors
def dynamic_colors(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

#Creating Map with latitudes

map = folium.Map(location=[38.58, -98.596944444444445], zoom_start=6, tiles="CartoDB positron")



#Adding objects to the Map throw a Feature Group

fgv = folium.FeatureGroup(name="Volcanoes")


for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=6,
                                     popup= str(el)+" m",
                                     fill_color=dynamic_colors(el),
                                     color ='grey',
                                     fill=True,
                                     fill_opacity=0.7))


#Adding Polygon Layer and Color to Differents Populations

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding= 'utf-8-sig').read(),
              style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                                  else 'orange' if 10000000 <=x['properties']['POP2005']<20000000
                                  else 'red'}))

map.add_child(fgv)  #Converts Volcanoes as Single Layer for LayerControl

map.add_child(fgp)  #Converts Population as Single Layer for LayerControl

#Adding Box for Controlling Layers
map.add_child(folium.LayerControl()) #Takes add_child as single elements for a big box

#Saves everything into a HTMLfile
map.save("Interactive Map.html")