def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
    
print(xo('xoox'))
print(xo('vmvfmvmn'))
print(xo('xxooo'))
print(xo('zzoo'))
print(xo('xxzzoO'))
#Проверьте, имеет ли строка одинаковое количество символов «х» и «о». 
# Метод должен возвращать логическое значение и быть нечувствительным к регистру. 
#Строка может содержать любой символ.
