f = open("demo.txt" "r")

data = f.read()
print(data)
print(type(data))


with open("sanjeev.txt", "r") as f:

    data = f.read()

    print(data)


f = open("simple.txt", "w")
f.close()

f = open("simple.txt", "a")
f.write("I am sanjeev Kumar")
f.close()


import os
os.remove("sanjeev.txt")