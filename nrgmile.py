# Relevant imports. Main.py holds most of the important functions used here.
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

#find total elevation gain and total elevation loss
gain = 0
loss = 0
for i in range(0,len(alt)-1):
    diff = alt[i+1] - alt[i]
    if diff > 0:
        gain += diff
    else:
        loss += abs(diff)
print("Total Distance Traveled: " + str(max(dist)) + " miles")
print("Total Elevation Gain: " + str(gain) + " feet")
print("Total Elevation Loss: " + str(loss) + " feet")

# call our interpolation function to get our z values. This uses natural cubic spline interpolation.
z=interp(dist,alt)

# find and print the energy miles using composite simpson's rule. Check the main.py file for these functions.
energy_miles = integrate_simp(dist,alt,z).norm
print("NRGmile rating: " + str(energy_miles) + " energy miles")

# find and print the energy miles with effect of altitude using composite simpson's rule. Check the main.py file for these functions.
energy_miles_alt = integrate_simp(dist,alt,z).alt
print("NRGmile rating (with altitude effect): " + str(energy_miles_alt) + " energy miles")

# below code finds the optimal segments for evenly distributing energy miles.
num_days = 4
segments = segment_solver(dist, alt, z, energy_miles, num_days)
print("In order to evenly distribute your energy miles you should hit the follow mileage at the end of each day: \n")
for i in range(0,num_days):
    print("Day " + str(i+1) + ": " + "Mile " + str(segments[i]) + "\n")