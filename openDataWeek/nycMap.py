import folium

mapCUNY = folium.Map(location=[40.768731, -73.964915], zoom_start=13, tiles="cartodbpositron" )

#folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nyc.html')
