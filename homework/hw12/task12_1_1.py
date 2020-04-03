def validate_pin(pin):
    return True if pin.isdigit() and (len(pin) == 4 or len(pin) == 6) else False

print(validate_pin('123456'))
print(validate_pin('12345'))
print(validate_pin('12345a'))
print(validate_pin('1234'))
print(validate_pin('aaaa'))

#Банкоматы допускают 4 или 6-значные ПИН-коды, 
# а ПИН-коды не могут содержать ничего, кроме 4 цифр или 6 цифр.
#Если функции передана правильная строка PIN, верните true, иначе верните false.