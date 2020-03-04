from math import *

x = int(input("Enter x: "))

y = (e**(2*x)*x**1/2-((x+1/3)/x))**0.5 * abs(cos(2.5*x))
print(y)
