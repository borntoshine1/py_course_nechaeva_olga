def is_square(n):    
    a = n**0.5
    if n < 0 or a%1 != 0:
        return False
    else:
        return True
    
print(is_square(-1))
print(is_square(0))
print(is_square(25))
print(is_square(26))

#Учитывая целое число, 
# определите, является ли оно квадратным числом