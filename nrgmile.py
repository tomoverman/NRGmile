# Relevant imports
from main import *
import csv

# read in CSV of interest. Should have two columns, col one with the distance traveled (miles) and col two with the altitude (feet).
# the CSV should also have a header row to work properly and not miss the first point.
table = csv.reader(open('examples/guad.csv'))
# skip the header row
next(table)
dist = []
alt=[]
# loop through the csv data and store in lists
for row in table:
    dist.append(float(row[0]))
    alt.append(float(row[1]))
# call our interpolation function to get our z values. This uses natural cubic spline interpolation.
z=interp(dist,alt)
energy_miles = integrate_simp(dist,alt,z)
print(energy_miles)