def printer_error(s):
    s = sorted(s)
    s.reverse()
    a = s.index('m')
    new_lst = s[0:a]
    return str(len(new_lst))+ '/' + str(len(s))
    
print(printer_error('yyabcdefjklmmxyz'))
print(printer_error('abcdefjklmmxyz'))
print(printer_error('abcdefjklmmxyzmm'))

#Написать функцию printer_error, которая для данной строки выведет частоту ошибок (буквы от m до z) в виде строки, 
# представляющей рациональное число, числитель которого равен числу букв от m до z, а знаменатель -
# длину контрольной строки. Строка имеет длину, большую или равную единице, и содержит только буквы от a to z.
