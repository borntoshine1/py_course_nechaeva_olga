def remove_every_other(ml):
    new_ml = []
    for i in range(len(ml)):
        if i%2 == 0:
            new_ml.append(ml[i])
        i+=1
    return new_ml



print(remove_every_other(['Hello', 'Goodbye', 'Hello Again', 'Hello', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6]))

#Возьмите массив и удалите каждый второй элемент из этого массива. 
#Всегда оставляйте первый элемент и начинайте удаление со следующего элемента.