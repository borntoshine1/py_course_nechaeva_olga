import random

rand_lst = []

for i in range(0,30):
    n = random.randint(0,100)
    rand_lst.append(n)
print(rand_lst)

dicti = {'A': 0, 'B': 0, 'C': 0, 'E': 0, 'D': 0}
for i in rand_lst:
    if 100 >= i > 90:
        dicti['A'] += 1
    elif 90 >= i > 80:
        dicti['B'] += 1
    elif 80 >= i > 70:
        dicti['C'] += 1
    elif 70 >= i > 60:
        dicti['E'] += 1
    else:
        dicti['D'] += 1

for k, v in dicti.items():
    print(k, v)
         