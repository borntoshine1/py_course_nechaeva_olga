def printer_error(s):
    count = 0
    for i in s:
       if i >"m":
          count+=1
    return "{}/{}".format(count, len(s))
    
print(printer_error('wyaabdemmwz'))
print(printer_error("wyzaamm"))
print(printer_error("wyzaamm, ,k m "))

#«хорошая» управляющая строка будет от а-m (aaabbbbhaijjjm), "плохая строка" от m-z. Вы должны написать функцию printer_error,
# которая для данной строки выведет частоту ошибок в виде строки, числитель которого равен числу ошибок, 
# а знаменатель - длину контрольной строки. Не уменьшайте эту дробь до более простого выражения.
# Строка имеет длину, большую или равную единице, и содержит только буквы от ato z.
