lst = [11, -2, 0, 9, 12, 51, 31]
lst1 = []

i = 1
while i < len(lst):
    if lst[i] % i == 0:
        lst1.append(lst[i])
    i += 1
print(lst1)
