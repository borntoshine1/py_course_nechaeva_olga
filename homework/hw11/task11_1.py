def duplicate_encode(word):
    my_str = ""
    word = word.lower()
    for i in word:
        if word.count(i) >= 2:
            my_str += ')'
        else:
            my_str += '('      
    return my_str

print(duplicate_encode("(( @"))
print(duplicate_encode("aasdf"))
print(duplicate_encode("qwer"))
print(duplicate_encode("zzxxccz"))
#Цель этого упражнения - преобразовать строку в новую строку, 
# где каждый символ в новой строке имеет место, "("
# если этот символ появляется только один раз в исходной строке 
# или ")"если этот символ появляется более одного раза в 
# исходной строке. Игнорировать заглавные буквы при определении, 
# является ли персонаж дубликатом.
