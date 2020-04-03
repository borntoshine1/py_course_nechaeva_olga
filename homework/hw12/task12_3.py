def is_isogram(string):
    s = string.lower()
    a = set(s)
    return True if len(string) == len(a) else False

print(is_isogram('zxcVz'))
print(is_isogram('zxcVa'))
print(is_isogram('zxcz'))
print(is_isogram(''))

#Изограмма - это слово, которое не имеет повторяющихся букв, 
# последовательных или непоследовательных. Реализуйте функцию, которая определяет, 
# является ли строка, содержащая только буквы, изограммой. 
# Предположим, что пустая строка является изограммой. Игнорировать регистр букв.