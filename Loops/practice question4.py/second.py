# search for a number x in this tuple using loop:

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 49, 100)

x = 49
idx = 0

for el in num:
    if (el == x):
        print("number found", idx)
    idx += 1


x = 49
idx = 0
for el in num:
    if(el == x):
        print("number found", idx)
        break
    idx += 1