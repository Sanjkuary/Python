#WAP to figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built-in data types)

values = {9, "9.0"}
print(values) # output = {9, '9.0'}

#we can also save it in the pair in the form of tuples.

values = {
    ("float" , 9.0),
    ("int", 9)
}

print(values) # output = {('int', 9), ('float', 9.0)}


