"""
Test driver for Program 14
Fall 2021
"""

import pandas as pd
import numpy as np
import p14

#Load the csv of libary locations:
lib = pd.read_csv('LIBRARY.csv')

#Apply the function to the DataFrame that creates a title column.
#   Note we need "axix=1" so that it works row by row:
lib["Title"] = lib.apply(p14.extractTitle,axis=1)
#Apply the function that extracts latitude and longitude.  We work row by row
#   and since it returns two values, we expand it to enter as two distinct columns:
lib[['Lon','Lat']] = lib.apply(p14.extractLatLon,axis=1,result_type='expand')

"""
Quick print to see the new columns.  The first three lines should be:
                                  Title        Lat        Lon
0         115th Street, New York, 10026  40.802980 -73.953531
1         125th Street, New York, 10035  40.803018 -73.934848
"""
print(lib[["Title","Lat","Lon"]])
