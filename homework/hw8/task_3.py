lst_my = [0, 1, -2, -2, -1, 3, 2, -11]
print("Old list - {}".format(lst_my))
sumnum = 0
count = 0
for i in lst_my:
    if i < 0:
        sumnum += i
        count+=1

average = (sumnum/count)
#print(delt)

mini = lst_my[0]
count2 =0
i=0
while i < len(lst_my):
    if lst_my[i] < mini:
        mini = lst_my[i]
        count2 = i
    i+=1    
#print(count2)
#print(mini)
lst_my[count2] = average
print("New list - {}".format(lst_my))