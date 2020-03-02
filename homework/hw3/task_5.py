from math import *

x = int(input("Enter x: "))

y = (e**(-2+x)**1/5) * 1/(x**2+x**4+log(abs(x-3.14)))
print(y)