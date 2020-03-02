from math import *

x = float(input("Enter x: "))

y = ((log10(acos(abs(x**3.4+2.5*x**1.2-0.7))/(e**(2.5*x))**1/3))**1/4) + 1
print(y)
#работает при условии х <= 0.6 и х > -0.2 примерно