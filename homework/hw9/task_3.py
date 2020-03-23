str_numb = input("Enter a set of numbers: ")

set_numb = set(str_numb)
#print(str_numb)
if str_numb.isdigit() == True:
    if len(str_numb) == len(set_numb):
        print("Unique set")
    else:
        print("Not a unique set")
else:
    print("Error")

