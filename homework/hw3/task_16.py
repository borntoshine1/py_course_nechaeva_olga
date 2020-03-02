from math import *

x = int(input("Enter x: "))

y = atan((abs(8.3-21*x**2-0.8*x))/(2.5+1/x**2)**1/3)
print(y)