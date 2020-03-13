lst1 = [1, 2, 31]
lst2 = [2, 32, 33, 4]


sum = len(lst1) + len(lst2)

print("|row_1|row_2|sum|")

if len(lst1) > len(lst2):
    print("|  {}  |  {}  |  {} | The first row is longer".format(len(lst1), len(lst2), sum))
elif len(lst1) < len(lst2):
    print("|  {}  |  {}  |  {} | The second row is longer".format(len(lst1), len(lst2), sum))
else:
    print("|  {}  |  {}  |  {} | Equal row".format(len(lst1), len(lst2), sum))


#если программа будет считать не колличество элементов, а их сумму 
#sum_1 = 0
#for i in lst1:
#    sum_1 = i + sum_1
#print(sum_1)
#sum_2 = 0
#for i in lst2:
#    sum_2 = i + sum_2
#print(sum_2)
#sum = sum_1 + sum_2
#if sum_1 > sum_2:
#    print("|  {}  |  {}  |  {} | The first row is longer".format(sum_1, sum_2, sum))
#elif sum_1 < sum_2:
#    print("|  {}  |  {}  |  {} | The second row is longer".format(sum_1, sum_2, sum))
#else:
#    print("|  {}  |  {}  |  {} | Equal row".format(sum_1, sum_2, sum))