#!/usr/bin/env python
import sys

current_boro = None
current_count = 0
boro = None
crime = None
stats = {}
stats2 = {}

for line in sys.stdin:
    line = line.strip()
    
    boro, statLine = line.split('\t')
    crime, count = statLine
    print (crime)
    print (count)
    try:
      count = int(count)
    except ValueError:
      continue
    if current_boro == boro:
      current_count += count
      stats[current_boro] = current_count
      stats2[current_boro] = current_count
    else:
      if current_boro: 
        print ('%s\t%s' % (current_boro, current_count))
      current_count = count
      current_boro = boro
      stats[current_boro] = current_count
      
if current_boro == boro:
  print ('%s\t%s' % (current_boro, current_count))
  
keymax = max(zip(stats.values(), stats.keys()))[1]
print("Most of the crimes were reported in " + keymax)
print("Total number of crimes reported in " + keymax + " is " + str(stats[keymax]))

      
        

    # rest of the code goes here ...
