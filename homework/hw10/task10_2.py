roles = {
  'Admin' : ["Valera", "Dan", "Jim"],
  'Maintainer' : ["Ben", "Fill", "Joe"],
  'Manager' : ["Juli", "David", "Vera"],
  'Developer' : ["Leo", "Neo", "Sam"],
}
name = input("Enter name: ")
for key, value in roles.items():
    if name in value:
        print("Hello, {}".format(key))
    else:
        print("Hello, Guest!")
        break 
        
