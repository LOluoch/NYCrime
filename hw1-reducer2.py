#!/usr/bin/env python3
from csv import reader
import sys


months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
month_count = {}
curr_month, curr_count = None, None

for line in sys.stdin:
    month, count = line.strip().split('\t', 1)
    month = int(month)
    count = int(count)

    if(month == curr_month):
        curr_count += count
    else:
        if curr_month:
            month_count[months[curr_month]] = curr_count
        curr_month = month
        curr_count = count

if month == curr_month:
    month_count[months[curr_month]] = curr_count

print("DANGEROUS WEAPONS reported per month:")
for each_month in months.values():
    print("%s %s" % (each_month, month_count.get(each_month, 0)))



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