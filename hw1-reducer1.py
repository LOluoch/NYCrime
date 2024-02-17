#!/usr/bin/env python
from csv import reader
import sys

boro_count, crime_type = dict(), dict()
curr_boro, curr_count, curr_crime = None

for line in reader(sys.stdin):
    boro, crime, count = line.strip().split('/t', 2)
    count = int(count)

    if(boro == curr_boro):
        curr_count += count
        curr_crime.add(crime)
    else:
        if curr_boro:
            boro_count[curr_boro] = curr_count
            crime_type[curr_boro] = curr_crime
        curr_boro = boro
        curr_count = count
        curr_crime = set()

if boro == curr_boro:
    boro_count[curr_boro] = curr_count
    crime_type[curr_boro] = curr_crime

highest_crime_location = max(boro_count, key = boro_count.get)
print("Most of the crimes were reported in %s" % highest_crime_location)
print("Total number of crimes reported in %s is %s" % (highest_crime_location, boro_count[highest_crime_location]))
print("Crime types reported in %s are %s" % (highest_crime_location, crime_type[highest_crime_location]))

# Write a MapReduce program in Python 3 (hw1-mapper1.py and hw1-reducer1.py) that will answer the
# following based on New York City Crime Data 2016. Run the program with only one reduce task.
# a) Where is most of the crime happening in New York? (e.g BRONX, QUEENS, BROOKLYN, etc.)
# b) What is the total number of crimes reported in that location ?
# c) What types of crime are happening in that location (show unique crime types) ?


