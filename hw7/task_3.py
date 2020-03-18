name = input("Enter your name please: ")
split_name = name.split()
len_name = len(name.split())

if len_name == 2:
    if split_name[0].isalpha() == True and split_name[1].isalpha() == True:
        print(split_name[0][0:1:] + "." + split_name[1][0:1:] + ".")
    else:
        print("Error: enter only letters")
else:
    print("Error: invalid name entry!")