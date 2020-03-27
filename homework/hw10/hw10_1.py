family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 5),
  'son_young' : ('Mark', 11)
}
mini = 200
for value in family.values():
    if mini > value[1]:
        mini = value[1]
print(mini)
