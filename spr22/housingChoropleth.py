"""
schoolsChoropleth.py:  code demo for Lecture #8
CSci 39542:  Introduction to Data Science
Hunter College, City University of New York

Updated with ideas from:  https://towardsdatascience.com/using-folium-to-generate-choropleth-map-with-customised-tooltips-12e4cec42af2
"""

import pandas as pd
import folium

#Load in the geoJSON districts from OpenData NYC:
nta_geo = "nta.geojson"
#Names of infile, outfile, column displayed, and year:
inFile = "Housing_Database_by_NTA.csv"
outFile = "netHousingUnits.html"
col = "total"

#Open the file into a DataFrame:
df = pd.read_csv(inFile)
#Make sure the data is numerical:
df['total'] = df['total'].astype(int)

#Center map at Hunter:  40.7678° N, 73.9645° W
m = folium.Map(location=[40.7678,-73.9645],zoom_start=10.5,tiles="cartodbpositron")

#Add in a choice of map tiles & icon to switch layers:
tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
for tile in tiles:
    folium.TileLayer(tile).add_to(m)

#Set the legend title to use the year and column selected:
legendTitle = f"Growth in Housing Units, 2010-2019"

#Set up the shading (choropleth) map based on total values:

choropleth = folium.Choropleth(
   geo_data=nta_geo,
   name="choropleth",
   data=df,
   columns=["nta2010","total"],
   key_on="feature.properties.ntacode",
   fill_color="Blues",
   fill_opacity=0.75,
   line_opacity=0.75,
   #threshold_scale = [0,20,40,60,80,100],
   legend_name=legendTitle,
   highlight = True
).add_to(m)

#Add in the layer with the shading:
folium.LayerControl().add_to(m)
'''
#Add the labels when hovering:
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['total'], labels=True))
'''
#Save the html to the specified output file:
m.save(outFile)
