def is_square(n):
    return False if n < 0 or (n**0.5)%1 != 0 else True     
    
print(is_square(-1))
print(is_square(0))
print(is_square(25))
print(is_square(26))

#Учитывая целое число, 
# определите, является ли оно квадратным числом
