lst1 = [1, 2, 31, 1]
lst2 = [2, 32, 32, 1]

if len(lst1) > len(lst2):
    print("The first row is longer")
elif len(lst1) < len(lst2):
    print("The second row is longer")
else:
    print("|row_1|row_2|sum|")
    j = 0
    for i in lst1:
        sum_row = i + lst2[j]
        print("| {} | {} | {} |".format(i, lst2[j], sum_row))
        j+=1
