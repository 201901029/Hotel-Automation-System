from datetime import *

def compare_dates(s1,s2):
    m1, d1, y1 = [int(x) for x in s1.split('/')]
  
    b1 = date(y1, m1, d1)
  
# Input for second date
    m2, d2, y2 = [int(x) for x in s2.split('/')]
  
    b2 = date(y2, m2, d2)
  
# Check the dates
    if b1 == b2:
        return 0;
      
    elif b1 > b2:
        return 1;
      
    else:
        return 0;


print(compare_dates("3/28/2023","4/21/2022"))