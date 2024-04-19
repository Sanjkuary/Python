nums = [1, 2, 3, 4, 5, 6] #list

for val in nums:
    print(val)

veg = ["ptato", "tomato", "cabbage", "ladyfinger"]
for val in veg:
    print(val)

str = ("Sanjeev Kumar") #str
for val in str:
    print(val)

tup = (1, 2, 3, 4, 5) #tuple

for num in tup:
    print(num)
else:
    print("end loop")


str = "sanjeev kumar" #use of else when any stoping condition.
for char in str:
    if(char == "k"):
        print("found", char)
        break
    print(char)
else:
    print("END")