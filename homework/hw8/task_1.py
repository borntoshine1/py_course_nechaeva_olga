import random

secret_number = random.randint(1, 50)

print(secret_number)

your_numb = int(input("Enter number: "))
i = 0
while i <= 5:
    if secret_number == your_numb:
        print("Yes it`s number - " + str(your_numb))
        break
    else:
        print("No it's not it, try again!")
        if secret_number > your_numb:
			print("Secret number is greater")
		else:
			print("Secret number is less")
        your_numb = int(input("Enter number again: "))
    i+=1  
