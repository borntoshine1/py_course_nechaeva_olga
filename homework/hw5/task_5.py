num = int(input("Enter number - "))
r = [1, 3, 2, 6, 22, 31, 40]
for i in r:
    if num == 0:
        print("Error zero division!")
        break
    elif i % num == 0:
        print(i)  
        
