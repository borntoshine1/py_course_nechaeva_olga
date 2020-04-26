string = input("Enter your string: ")
symbol = input("Enter symbol: ")
new_string = ""

for i in string:
    new_string = string.replace(symbol, "")

print(new_string)
