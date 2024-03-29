#!/usr/bin/env python3
from csv import reader
import sys

for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime or boro == "BORO_NM":
        continue
    print("%s \t %s \t %s \t" % (boro, crime, 1))


# Write a MapReduce program in Python 3 (hw1-mapper1.py and hw1-reducer1.py) that will answer the
# following based on New York City Crime Data 2016. Run the program with only one reduce task.
# a) Where is most of the crime happening in New York? (e.g BRONX, QUEENS, BROOKLYN, etc.)
# b) What is the total number of crimes reported in that location ?
# c) What types of crime are happening in that location (show unique crime types) ?
