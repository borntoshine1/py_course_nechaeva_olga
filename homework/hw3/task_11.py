from math import *

x = int(input("Enter x: "))

y = acos(tan(5*x/pi)) + ((x**3.2)/28)
print(y)
# при вводе нечетного числа выдает ошибку т.к. тангенс получается больше -1.