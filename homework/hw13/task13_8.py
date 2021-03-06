def two_sum(numbers, target):
    i = 1
    j = 0
    while i < len(numbers):
        if numbers[i]+numbers[j] == target:
            return [j, i]
        if i==len(numbers)-1:
            j+=1
            i=j
        
        i+=1
    
print(two_sum([1,2,3,1,2], 4))
print(two_sum([2,2,3,1,3], 4))
print(two_sum([3,2,1], 4))
print(two_sum([1234,5678,9012], 14690))

#Напишите функцию, которая принимает массив чисел (целые числа для тестов) и целевое число. 
# Он должен найти два разных элемента в массиве, которые при сложении дают целевое значение. 
# Индексы этих элементов затем должны быть возвращены в кортеже следующим образом: (index1, index2).