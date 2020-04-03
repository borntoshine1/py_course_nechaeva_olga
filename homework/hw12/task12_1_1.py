def validate_pin(pin):
    return True if pin.isdigit() and (len(pin) == 4 or len(pin) == 6) else False

print(validate_pin('123456'))
print(validate_pin('12345'))
print(validate_pin('12345a'))
print(validate_pin('1234'))
print(validate_pin('aaaa'))