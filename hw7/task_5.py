old_str = input("Enter string: ")
old_str = old_str.split()
old_split_str = old_str[::-1]
new_str = " ".join(old_split_str)
print(new_str)