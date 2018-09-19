"""
 1 Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 

from datetime import date 
date_1= date(2014,1,8)
date_2= date(2014,1,30)

delta = date_2-date_1

print(delta.days)
"""



"""
2 Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""


def difference(a):
    if a>17:
        return (a-17)*2
    else:
        return 17-a

print(difference(22))
print(difference(14))
    
