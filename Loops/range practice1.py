# print numbers from i to 100.

for i in range(1, 101):
    print(i)

# print numbers form 100 to 1.
for i in range(100, 0, -1):
    print(i)


#print the multiplication of numer n.
n = int(input("enter number : "))

for i in range(1, 11):
    print(n * i)


#print the division on number n.

n = int(input("enter number : "))
for i in range(1, 11):
    print(n / i)


#using pass

for i in range(5):
    pass
if i > 5:
    pass
print("some useful work")