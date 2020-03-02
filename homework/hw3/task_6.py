from math import *

x = int(input("Enter x: "))

y = ((sin(x/2))**3)**1/2 + (e**(1.3*x)+e**(-1.3*x)**1/3) * 1/(abs(x+5/2))
print(y)