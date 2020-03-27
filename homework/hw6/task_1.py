lst = ['i love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']

num = int(input("Enter number - "))
print(lst[(num%len(lst))-1])
