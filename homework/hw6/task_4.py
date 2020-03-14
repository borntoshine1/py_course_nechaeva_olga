word = "olyylo"
#word = input("Enter word - ")

#list(word)
lst = list(word)
i=0
j = len(lst)
count = False
while i <= j:
    if lst[i] == lst[j-1]:
        i+=1
        j-=1
        count = True
    else:
        count = False
        break

if count == True:
    print("Еhis word is a palindrome")
else:
    print("Not palindrome")
