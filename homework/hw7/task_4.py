numbers = input("Enter string: ")
if numbers.isdigit():
    int_lst = [int(i)for i in numbers]
    for i in int_lst:
        if i >=5:
            print("1", end="")
        else:
            print("0",end="")
else:
    print("Error: enter only numbers")

print()