def row_sum_odd_numbers(n):
    return sum(range((n-1)**2+n, n**2+(n), 2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(30))
print(row_sum_odd_numbers(5))

#Учитывая треугольник последовательных нечетных чисел вывести сумму строки n

#             1
#          3     5
#      7     9    11
#  13    15    17    19
#21    23    25    27    29
