def sum_of_minimums(numbers):
    sum_numb=0
    for i in numbers:
        sum_numb += min(i)
    return sum_numb
    
print(sum_of_minimums([[ 7,9,8,6,2 ],[6,3,5,4,3],[5,8,7,4,5] ]))
print(sum_of_minimums([[11,12,14,54],[67,89,56],[7,9,4,3],[9,8,6,7]]))

#Дан двухмерный список размером m * n. 
#Ваша задача - найти сумму минимальных значений каждой строки.