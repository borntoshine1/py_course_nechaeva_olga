def get_count(inputStr):
    return len([i for i in inputStr if i in 'aeiou'])

print(get_count('aeui'))
print(get_count('aeuiw   eu'))
print(get_count('awwrr eiou'))

#Вернуть количество (count) гласных в данной строке. Мы будем рассматривать a, e, i, o и u как гласные.
# Входная строка будет состоять только из строчных букв и / или пробелов.