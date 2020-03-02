from math import *

x = int(input("Enter x: "))

y = 2*pi*x - (abs(sin((10.5*x)**1/2))) * (1/((x**2)**1/3)+1/7)
print(y)