def dasemvowel(string):
    new_lst=[]
    for i in list(string):
        if i.lower() not in "aeiuo":
            new_lst+=[i]
            new_str = "".join(new_lst)
    return new_str

print(dasemvowel("SaEdru"))
print(dasemvowel("LOL"))
print(dasemvowel("HeLLo WOrLd"))

# убрать гласные "aeiuo" из строки