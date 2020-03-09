list = [1,2,3,4,5,6,7,8,9,10,1]
i = 0
while i < len(list):
    if i+1 == len(list):
        print("The list is ordered \n{}".format(list))
        break
    elif list[i+1] - list[i] == 1:
        i +=1 
    else:
         print(list[i+1])
         break
    
