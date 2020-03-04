from math import *

x = int(input("Enter x: "))

y = acos(tan(5*x/pi)) + x**5.7/23
print(y)
# при вводе нечетного числа выдает ошибку т.к. тангенс получается больше -1.