def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum_two = numbers[0] + numbers[1]
    return sum_two
print(sum_two_smallest_numbers([2, 5, 1, 3]))
print(sum_two_smallest_numbers([2, 0, 1, 3]))
print(sum_two_smallest_numbers([2, 15, 11, 3]))
#Создайте функцию, которая возвращает сумму двух наименьших положительных чисел, 
#учитывая массив из минимум 4 положительных чисел. 
#Никакие числа с плавающей точкой или неположительные целые числа не будут переданы.