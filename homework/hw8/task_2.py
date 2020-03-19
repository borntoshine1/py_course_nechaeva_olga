my_lst = [1, 1, 10, 2, -3, -4, 2, 3, -4, 6, 10]
count = 0

for i in my_lst:
    if i >= 0:
        count +=1
        if count == 1:
            per = i
            print(i)
        elif count == 3:
            per2 = per * i
            print(i)
        elif count == 6:
            per3 = per2 * i
            print(i)
            print(per3) 


       
