def in_asc_order(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(in_asc_order([1, 2, 3]))
print(in_asc_order([1, 3, 2]))
print(in_asc_order([1, 2, 2, 3, 5]))
print(in_asc_order([1, 2, 2, 3, 5, 4]))

#В этом задания ваша функция получает массив целых чисел в качестве входных данных.
#Ваша задача - определить, находятся ли числа в порядке возрастания.