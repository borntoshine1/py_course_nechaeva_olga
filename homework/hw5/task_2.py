num = int(input("Enter number - "))
n1 = 1
n2 = 1
n3 = n1 +n2
print(n1, end=' ')
print(n2, end=' ')
print(n3, end=' ')
sum = 0
while num > sum:
    sum = n3 + n2
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    if num > sum:
        print(sum, end=' ')

    
