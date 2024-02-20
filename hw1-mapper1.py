#!/usr/bin/env python
from csv import reader
import sys

for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip()) # Loop through rows to get boro, crime vars
    if not boro or not crime or boro == "BORO_NM":
        continue
    print ('%s\t%s' % (boro, [crime, 1]))
       

    # rest of the code goes here ...
