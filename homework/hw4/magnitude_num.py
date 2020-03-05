from math import *

num_1 = int(input('Enter first number - '))
num_2 = int(input('Enter second number - '))

if abs(num_1) > abs(num_2):
    print('The absolute value of the first number {} is greater'.format(num_1))
elif abs(num_2) > abs(num_1):
     print('The absolute value of the second number {} is greater'.format(num_2))
else:
    print('The absolute value of two numbers equal')