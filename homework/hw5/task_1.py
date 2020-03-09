list = [22, 2, 33, -1, 4, 5]
min = list[0]
i = 0
while i < len(list):
    if  list[i] < min:
        min = list[i]
        i += 1
    else:
        i += 1
print(min)