lst = ["sheep", "sheep", "sheep", "sheep", "wolf", "sheep", "sheep"]
lst.reverse()
i = 1
while i < len(lst):
    if lst[i-1] == "sheep" and lst[i] == "wolf":
        print("Oi! Sheep number {} ! You are about to be eaten by a wolf!".format(i))
        break        
    elif lst[i-1] == "wolf" and lst[i] == "sheep":
        print("Pls go away and stop eating my sheep")
        i+=1
    else:
        i+=1       
    
