#WAP to enter marks of 3 subjects form the user and store them in dictionary.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)