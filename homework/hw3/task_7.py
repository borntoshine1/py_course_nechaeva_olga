from math import *

x = int(input("Enter x: "))

y = ((abs(x*log(x)-4))*x**1/2) * 1/(e**(4*x-1))**1/5
print(y)