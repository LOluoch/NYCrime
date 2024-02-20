

#!/usr/bin/env python3
import sys
from datetime import datetime

current_month = None
current_count = 0
stats = {}

for line in sys.stdin:
    line = line.strip()
    crime, date = line.split('\t', 1)

    date_object = datetime.strptime(date, "%m/%d/%Y")
    try:
      month = date_object.strftime("%B")
    except ValueError:
      continue
    
    if crime == "DANGEROUS WEAPONS" and date_object.strftime("%Y")=="2016":
      if current_month == month:
        current_count += 1
        stats[current_month] = current_count
        
      else:
        current_count = 1
        current_month = month
        stats[current_month] = current_count  
        


#keymax = max(zip(stats.values(), stats.keys()))[1]
print("DANGEROUS WEAPONS reported per month:")
for key, value in stats.items():
    print(key,value)

