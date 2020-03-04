from math import *

x = int(input("Enter x: "))

y = asin((log10(x))/(x**2+5*x+1)) - x**3.2/28
print(y)