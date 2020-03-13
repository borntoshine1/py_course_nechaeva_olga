lst = ['i love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']

num = int(input("Enter number - "))

i = 1
j = 0
while i <= num:
    if j == len(lst):
        j = 0
    i+=1
    j+=1
print(lst[j-1])
    