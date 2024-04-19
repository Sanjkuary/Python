a = int(input("Enter First number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
d = int(input("Enter fouth number :"))

if(a >= b and a >= c and a >= d):
    print("First number is largest", a)
elif(b >= a and b >= c and b >= d):
    print("second umnber is largest", b)
elif(c >= a and c >= b and c >= d):
    print("thitd umnber is largest", c) 
else:
    print("fouth number is largest", d)