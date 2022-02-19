"""
schoolsChoropleth.py:  code demo for Lecture #8
CSci 39542:  Introduction to Data Science
Hunter College, City University of New York

Updated with ideas from:  https://towardsdatascience.com/using-folium-to-generate-choropleth-map-with-customised-tooltips-12e4cec42af2
"""

import pandas as pd
import folium

#Load in the geoJSON districts from OpenData NYC:
school_geo = "SchoolDistricts.geojson"
#Names of infile, outfile, column displayed, and year:
inFile = "district-ela-results-2013-2019.csv"
outFile = "ela2019choropleth.html"
col = "% Level 3+4"
year = 2019

#Open the file into a DataFrame:
df = pd.read_csv(inFile)
#Set the district to be a string to match the type in the geoJSON file:
df['District'] = df['District'].astype(str)

#Select only the year's results
dfSingleYear = df[df['Year'] == year]

#Center map at Hunter:  40.7678° N, 73.9645° W
m = folium.Map(location=[40.7678,-73.9645],scale=13,tiles="cartodbpositron")

#Add in a choice of map tiles & icon to switch layers:
tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
for tile in tiles:
    folium.TileLayer(tile).add_to(m)

#Set the legend title to use the year and column selected:
legendTitle = f"{year} ELA Scores ({col})"

#Set up the shading (choropleth) map based on school district values for col:
choropleth = folium.Choropleth(
   geo_data=school_geo,
   name="choropleth",
   data=dfSingleYear,
   columns=["District",col],
   key_on="properties.school_dist",
   fill_color="Reds",
   fill_opacity=0.75,
   line_opacity=0.75,
   threshold_scale = [0,20,40,60,80,100],
   legend_name=legendTitle,
   highlight = True
).add_to(m)

#Add in the layer with the shading:
folium.LayerControl().add_to(m)
#Add the labels when hovering:
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['school_dist'], labels=True))

#Save the html to the specified output file:
m.save(outFile)
