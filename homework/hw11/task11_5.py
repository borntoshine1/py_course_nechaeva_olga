def century(year):
    return year//100 if year%100 == 0 else (year//100)+1
      
century(1)
century(2000)
century(1991)
century(2001)

#Первые пролеты века от года 1 до и включая 100 года, 
# второй - от года до 101 включительно 200 года, и т.д.
