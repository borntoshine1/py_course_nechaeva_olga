def century(year):
    a = year//100
    #print(a)
    if year%100 == 0:
        return print(a)
    else:
        return print(a+1)

century(1)
century(2000)
century(1991)
century(2001)

#Первые пролеты века от года 1 до и включая 100 года, 
# второй - от года до 101 включительно 200 года, и т.д.