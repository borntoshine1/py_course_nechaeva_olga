family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 15),
  'son_young' : ('Mark', 9)
}
    
#new_lst = []
for value in family.values():
  new_lst=[]
	new_lst.append(value[1])
print(max(new_lst)-min(new_lst)) 
