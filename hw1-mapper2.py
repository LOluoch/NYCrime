#!/usr/bin/env python3
from csv import reader
import sys

for line in reader(sys.stdin):
    date, crime = (line[5].strip(), line[7].strip()) 
    if not date or not crime or date == "RPT_DT":
        continue
    print ('%s\t%s' % (crime, date))
     

    # rest of the code goes here ...
