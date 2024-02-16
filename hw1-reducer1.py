# Write a MapReduce program in Python 3 (hw1-mapper1.py and hw1-reducer1.py) that will answer the
# following based on New York City Crime Data 2016. Run the program with only one reduce task.
# a) Where is most of the crime happening in New York? (e.g BRONX, QUEENS, BROOKLYN, etc.)
# b) What is the total number of crimes reported in that location ?
# c) What types of crime are happening in that location (show unique crime types) ?



#!/usr/bin/env python
import sys

current_boro = None
current_count = 0
boro = None

for line in reader(sys.stdin):
    line = line.strip()
    boro, count = line.split('\t', 1)
    try:
      count = int(count)
    except ValueError:
      continue
    if current_boro == boro:
      current_count += count
    else:
      if current_boro: #Isn't this going to be false??? Shouldn't it be boro for first loop?
        print ('%s\t%s' % (current_boro, current_count))
      current_count = count
      current_boro = boro
      
if current_boro == boro:
  print ('%s\t%s' % (current_boro, current_count))
      
        

    # rest of the code goes here ...
