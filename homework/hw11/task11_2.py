def binary_array_to_number(arr):
    number = 0
    for i in range(0, len(arr)):
        number = number+int(arr[i])*(2**(len(arr)-i-1))
    return number


print(binary_array_to_number([0,0,1,1]))
print(binary_array_to_number([0,1,1,1]))
print(binary_array_to_number([1,0,1,1]))
print(binary_array_to_number([1,1,1,1]))
#Учитывая массив единиц и нулей, 
#преобразовать эквивалентное двоичное значение в целое число.