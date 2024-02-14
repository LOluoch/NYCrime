# Write a MapReduce program in Python 3 (hw1-mapper2.py and hw1-reducer2.py) that will answer the
# following based on New York City Crime Data 2016. Run the program with two reduce tasks.
# How many crimes of type “DANGEROUS WEAPONS” were reported on each month of the year 2016 ?
# Sample Output:
# Most of the crimes were reported in XYZ.
# Total number of crimes reported in XYZ is ....
# Crime types reported in XYZ are ....
# DANGEROUS WEAPONS reported per month:
# January ###
# February ###
# ..
# ..
# December ###


#!/usr/bin/env python
from csv import reader
import sys

for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime or boro == "BORO_NM":
        continue

    # rest of the code goes here ...

    # rest of the code goes here ...
